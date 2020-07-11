# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: py,ipynb
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.5.1
#   kernelspec:
#     display_name: Python 3.8.3 64-bit
#     language: python
#     name: python38364bita14c50cabb94433e97ec307454e1294b
# ---

# # 物理单位和物理常量

# +
# # %pip install -U astropy
# -

# ## 单位 [units](https://docs.astropy.org/en/stable/units/#module-astropy.units) 

import astropy.units as u

# ### 查看 units 的 attributes

len(dir(u)), dir(u)

# ### 单位运算

S = u.m * (u.kg * u.m / u.s)
S

# #### 不同的单位可能有相同的量纲

S.compose()    # 或 u.parsec

u.eV.compose()

u.degree.compose()

# ### 带单位量 ([Quantity](https://docs.astropy.org/en/stable/api/astropy.units.Quantity.html#astropy.units.Quantity))

q = 60. * u.arcmin
q

qs = [60., 3600.] * u.arcsec

# #### 带单位量的转换

q.to(u.degree)

qs.to(u.deg)

# #### 对等 ([equivalencies](https://docs.astropy.org/en/stable/units/equivalencies.html#unit-equivalencies)) 转换

(1000 * u.nm).to(u.Hz, equivalencies=u.spectral())

# #### 单位比较

u.isclose(1. * u.eV, 1.60218e-19 * u.J)

# ### 单位制

u.eV.cgs

# ## 常量 [constants](https://docs.astropy.org/en/stable/constants/)

from astropy import constants as const

const.c

const.hbar

print(const.c)

print(const.hbar)

from astropy import uncertainty as unc

a = unc.normal([1, 2]*u.kpc, std=[30, 50]*u.pc, n_samples=100000)

a

a.pdf_mean()

a.pdf_std()

# # 表格 [Table](https://docs.astropy.org/en/stable/table/)

from astropy.table import Table

t = Table.read('../data/AF.csv')
t

t[0]

t['A']

t['A'] *= u.s
t

df = t.to_pandas()
df
