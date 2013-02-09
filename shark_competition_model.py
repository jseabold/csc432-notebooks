# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=3>

# Competition Model - White Tip Sharks vs Black Tip Sharps

# <markdowncell>

# * two species competing for resources
# * number of deaths is proportional to both pop. 
#   size and pop. size of other species
# * For population $B$ and population $W$, $\text{deaths}\propto BW$

# <markdowncell>

# $$\Delta\left(\text{births of WTS}\right)=g_{w}W$$
# $$\Delta\left(\text{births of BTS}\right)=g_{b}B$$
# $$\Delta\left(\text{deaths of WTS}\right) = d_{w}BW$$
# $$\Delta\left(\text{deaths of BTS}\right) = d_{b}BW$$
# 
# where $d_{w}$ and $d_{b}$ are the respective death proportionality constants for each species and
# $g_{w}$ and $g_{b}$ are the respective birth rates.

# <codecell>

# ordinary variables

bts_birth_fraction = 1.
bts_death_prop_const = .2
wts_birth_fraction = 1.
wts_death_prop_const = .27

# derived variables

# stock variables
# defined within solver

# define flow equations

def births(pop, birth_fraction):
    return pop*birth_fraction

def deaths(bts_pop, wts_pop, death_prop_const):
    return death_prop_const * bts_pop * wts_pop

# func(y, t, args)
def dpop_dt(pops, t, wts_birth_frac, 
            bts_birth_frac, wts_death_prop, 
            bts_death_prop):
    bts, wts = pops
    bts_born = births(bts, bts_birth_frac)
    wts_born = births(wts, wts_birth_frac)
    bts_change = bts_born - deaths(bts, wts, bts_death_prop)
    wts_change = wts_born - deaths(wts, bts, wts_death_prop)
    return [bts_change, wts_change]
    

# initial conditions

bts_population_0 = 15
wts_population_0 = 20

time_points = np.arange(0, 5, .1)

# <codecell>

from scipy import integrate
pops = integrate.odeint(dpop_dt, [bts_population_0,
                                  wts_population_0], 
                    time_points, args=(wts_birth_fraction, 
                                        bts_birth_fraction, 
                                        wts_death_prop_const,
                                        bts_death_prop_const)
                        )

# <codecell>

bts, wts = pops.T

# <codecell>

fig, ax = plt.subplots(subplot_kw=dict(xlabel="t (months)", 
                                       ylabel="population"),
                       figsize=(8,5)
                    )
ax.plot(time_points, bts, "k--", label="BTS", lw=2)
ax.plot(time_points, wts, "k-", label="WTS", lw=2);
ax.legend();

# <codecell>

import pandas
pandas.DataFrame(np.column_stack((time_points, pops)),
                 columns=["months", "BTS", "WTS"])

