<<<<<<< HEAD
cor_matrix = df.corr().abs()
print(cor_matrix)

upper_tri = cor_matrix.where(np.triu(np.ones(cor_matrix.shape),k=1).astype(np.bool))
print(upper_tri)

to_drop = [column for column in upper_tri.columns if any(upper_tri[column]  0.95)]
print(to_drop)

df1 = df.drop(df[to_drop], axis=1)
=======
cor_matrix = df.corr().abs()
print(cor_matrix)

upper_tri = cor_matrix.where(np.triu(np.ones(cor_matrix.shape),k=1).astype(np.bool))
print(upper_tri)

to_drop = [column for column in upper_tri.columns if any(upper_tri[column]  0.95)]
print(to_drop)

df1 = df.drop(df[to_drop], axis=1)
>>>>>>> 6666e992810116a56c2096b8ad94e572079a26e3
print(df1.head())