# grouping by but keeping group as variable rather than index
e = d.groupby(['group'], as_index=False).sum()

# converting columns to class variable 
pd.melt(e, id_vars='group'))
