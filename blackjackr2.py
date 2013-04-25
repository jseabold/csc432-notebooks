import numpy as np
import matplotlib.pyplot as plt
"""
I decided to make the shoe NumPy and the hand NOT NumPy.
It made sense to make the shoe NumPy, especially with larger decks.
That logic didn't seem to matter as much for individual hands.
I also just create a new deck when the shoe is up. Seems faster
and more logical.

Notes from last time:
Dealer stands iff dealer is hard 17.
Blackjack gets you your money immediately, as opposed to pushing if dealer also blackjacks.
The arbitrary truecount for these simulations will be +2.
    If truecount >= +2, players will not hit.
"""


class shoe:
    def __init__(self, size, deck = ["A",2,3,4,5,6,7,8,9,10,10,10,10],
                 decksets = 4):
        decksize = decksets * len(deck)
        self.deck = np.array(deck * decksize * size)
        #Marking when to use a new deck
        self.yellowcard = np.random.randint(self.deck.size/2,
                                            self.deck.size-30)
        #Counter towards the yellowcard
        self.count = 0
        self.reset = False
        np.random.shuffle(self.deck)

    def show(self):
        print(self.deck)

    def deal(self):
        self.count += 1
        if self.count > self.yellowcard :
            self.reset = True
        todeal = self.deck[0]
        if not todeal == "A":
            int(todeal)
        self.deck = np.delete(self.deck,0)
        return todeal


class player:
    def __init__(self,
                 bank,
                 lowbet = 25,
                 hibet = 100,
                 countsystem = {"2":1, "3":1, "4":1, "5":1, "6":1,
                                "7":0, "8":0, "9":0, "10":-1, "A":-1},
                 countaccuracy = 100
                 ):
        self.hand = []
        self.bank = bank
        self.low = lowbet
        self.high = hibet
        self.done = False
        self.bet = 0
        self.mycount = 0
        self.betbig = False
        self.countsystem = countsystem
        self.countaccuracy = countaccuracy

    def evalhand(self):
        """
        This method might be a bit redundant
        but it allows adjustment of hands to optimal
        value. It is useful post deal.
        """
        if(not 11 in self.hand and not 1 in self.hand):
            return sum(self.hand)
        else:
            while(sum(self.hand) > 21):
                if(11 in self.hand):
                    self.hand[self.hand.index(11)] = 1
                else:
                    break
            return sum(self.hand)

    def get(self,card):
        if(card == "A" and sum(self.hand) <= 10):
            self.hand.append(11)
        elif(card == "A"):
            self.hand.append(1)
        else:
            self.hand.append(int(card))

    def reset(self):
        self.hand = []

    def show(self):
        print(self.hand)

    def count(self,card):
        """
        Currently this only allows players to mis-read
        cards, i.e. not factoring them into count.
        """
        if(np.random.randint(0,self.countaccuracy + 1)):
            self.mycount += self.countsystem[card]

class dealer:
    def __init__(self):
        self.hand = []

    def evalhand(self):
        if(not 11 in self.hand and not 1 in self.hand):
            return sum(self.hand)
        else:
            while(sum(self.hand) > 21):
                if(11 in self.hand):
                    self.hand[self.hand.index(11)] = 1
                else:
                    break
            return sum(self.hand)

    def show(self):
        print(self.hand)

    def cardup(self):
        return self.hand[0]
    def reset(self):
        self.hand = []

    def get(self,card):
        if(card == "A" and sum(self.hand) <= 10):
            self.hand.append(11)
        elif(card == "A"):
            self.hand.append(1)
        else:
            self.hand.append(int(card))

#players = np.array([player(1000),player(1000)],dtype=object)
#players[:].get(x.deal())



def dealplayer(shoe,player,table):
    """
    This method handles dealing cards and counting.
    """
    dealing = shoe.deal()
    for card_counters in table:
        card_counters.count(dealing)
    player.get(dealing)

def runtest(num_players, iterations=1000, numdecks=1, initial_bank=1000,
            counting = True):
    tableshoe = shoe(numdecks)
    """
    Unsure if I want to make dealer part of the table.
    table = np.array([dealer()])
    table = np.append(table,[player(initial_bank) s
                             for z in range(num_players)])
    """
    tabledealer = dealer()
    table = np.array([player(initial_bank,countaccuracy = 50)
                      for z in range(num_players)])

    #Placing bets
    #HYPOTHESIS: A deck with high face cards is FAVORABLE
    #to the player. True count of 1 is arbitrary.
    for seat in table:
        if float(seat.mycount)/numdecks > 10:
            """
            This means there are 10 more high cards in the deck
            than low cards, thus an advantage to the player,
            which means they should bet bigger.
            """
            seat.betbig = True
        else:
            seat.betbig = False

    for z in range(iterations):

        #Initial deal
        for i in range(2):
            for seat in table:
                dealplayer(tableshoe,seat,table)
            dealplayer(tableshoe,tabledealer,table)

        #Check for blackjack
        for seat in table:
            if(seat.evalhand() == 21):
                seat.bank += seat.high * 1.5 if seat.betbig else seat.low * 1.5
                seat.done = True

        #Player options
        for seat in table:
            if(seat.done): continue
            while(seat.evalhand() <= 10):
                dealplayer(tableshoe,seat,table)
            if(tabledealer.cardup() in [7,8,9,10,1,11]):
                #If faceup card is 7-A
                while(seat.evalhand() <= 16):
                    dealplayer(tableshoe,seat,table)
            else:
                #If faceup card is 2-6
                while(seat.evalhand() <= 18):
                    dealplayer(tableshoe,seat,table)
            if(counting):
                #Arbitrary counting rule addition 1
                #print(float(seat.mycount)/numdecks)
                if(seat.evalhand() <= 12 and float(seat.mycount)/numdecks < -10):
                    dealplayer(tableshoe,seat,table)
                #Arbitrary counting rule addition 2
                if(seat.evalhand() <= 15 and float(seat.mycount)/numdecks < -15):
                    dealplayer(tableshoe,seat,table)
                seat.done = True
            else:
                seat.done

        #Dealer options
        while(tabledealer.evalhand() < 18):
            dealplayer(tableshoe,tabledealer,table)

        #Check if dealer busts
        if(tabledealer.evalhand() > 21):
            for seat in table:
                seat.bank += seat.high if seat.betbig else seat.low
        #Dealer checks for blackjack
        elif(tabledealer.evalhand() == 21):
            for seat in table:
                seat.bank -= seat.high if seat.betbig else seat.low
        else:
        #Evaluate remaining vs dealer
            for seat in table:
                #Couldn't make this one condition. Damn python short circuits.
                if (seat.evalhand() > 21):
                    seat.bank -= seat.high if seat.betbig else seat.low
                elif(tabledealer.evalhand() >= seat.evalhand()):
                    seat.bank -= seat.high if seat.betbig else seat.low
                else:
                    seat.bank += seat.high if seat.betbig else seat.low

        #Cleanup stage
        for seat in table:
            seat.done = False
            seat.hand = []
        if(tableshoe.reset):
            tableshoe = shoe(numdecks)
            for seat in table:
                seat.mycount = 0
        tabledealer.hand = []

    return np.array([seat.bank for seat in table])

def runlayer1():
    #Initialize elements that play 100 hands each
    myarray = np.array([runtest(1, numdecks = 1, iterations = 100,
                        counting = False) for z in range(100)])
    losers = np.where([myarray<1000])
    #print losers[1]
    #print len(losers[1])
    #Get return percentage of each element
    myarray = (myarray - 1000)/1000
    #Average return across all elements across 100 hands PER hand
    #print (sum(myarray)/100/100)
    #Average return across all elements across 100 hands
    return (sum(myarray)/100)


"""with open("mydata.txt","w") as f:
    for z in range(1):
        num = runlayer1()
        f.write(str((float(num))))
"""


if __name__ == "__main__":
    #job_server = pp.Server()
    #myarray = np.array([100])

    #f1 = job_server.submit(runlayer1(),(),(runtest,),("numpy as np",))
    #f2 = job_server.submit(runlayer1(),(),(runtest,),("numpy as np",))
    #mytarget = np.array([runlayer1() for z in range(10)])
    #print mytarget
    #plt.hist(mytarget)

    # before we do anything, let's do some benchmarking
    import cProfile
    import pstats

    cProfile.run('runlayer1()', 'speed_stats.prof')
    p = pstats.Stats('speed_stats.prof')
    # where do we spend the most time (includes sub-functions)
    p.strip_dirs().sort_stats('cumulative').print_stats(10)

    # where are we looping a lot
    p.strip_dirs().sort_stats('time').print_stats(10)

    # michael is spending a lot of time in delete, what's this used for?
    # Honestly, I've never even seen this function.

    # things to notice, almost a million function calls
    # http://docs.python.org/2/library/profile.html#instant-user-s-manual
    #ncalls
        #for the number of calls,
    #tottime
        #for the total time spent in the given function (and excluding time made in calls to sub-functions)
    #percall
        #is the quotient of tottime divided by ncalls
    #cumtime
        #is the cumulative time spent in this and all subfunctions (from invocation till exit). This figure is accurate even for recursive functions.

    #NOTE: Rethink using string arrays



