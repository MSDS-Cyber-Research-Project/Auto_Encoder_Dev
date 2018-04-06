import pandas as pd
import time

#let's measure how long it takes to import the dataset
start_time = time.time()

#df = pd.read_csv("/host/data/auth_only_logons.txt", sep=',', names = ["time","src_user","dest_user","src_nt_host","dest_nt_host","auth_type","logon_type","auth_orientation","action"])
df = pd.read_csv("/Users/alexaubrey/Documents/School/MSDS/Research Methods/project/auth_filtered_all_with_labels_sorted_2.txt", sep=',', names = ["time","src_user","dest_user","src_nt_host","dest_nt_host","is_malicious"])

print("Load data time:")
print(time.time() - start_time)

start_time_group_by = time.time()

#determine how many overall occurances does a particular src_user/changed_attribute have
df['dest_user_count'] = df.groupby('dest_user')['dest_user'].transform('count')

df['src_user_count'] = df.groupby('src_user')['src_user'].transform('count')

df['src_nt_host_count'] = df.groupby('src_nt_host')['src_nt_host'].transform('count')

df['dest_nt_host_count'] = df.groupby('dest_nt_host')['dest_nt_host'].transform('count')

df['total'], _ = df.shape

print("Group by times:")
print(time.time() - start_time_group_by)

### p(A|B) = p(AnB)/p(B)
### p(AnB) = p(A) * p(B)

prob_time = time.time()

df['p(src_user)'] = df['src_user_count'] / df['total']
df['p(dest_user)'] = df['dest_user_count'] / df['total']
df['p(src_nt_host)'] = df['src_nt_host_count'] / df['total']
df['p(dest_nt_host)'] = df['dest_nt_host_count'] / df['total']

### Joint probabilities
df['p(src_user n dest_user)'] = df['p(src_user)'] * df['p(dest_user)']
df['p(src_nt_host n dest_nt_host)'] = df['p(src_nt_host)'] * df['p(dest_nt_host)']
df['p(dest_user n dest_nt_host)'] = df['p(dest_user)'] * df['p(dest_nt_host)']

print("Joint Probability time:")
print(time.time() - prob_time)

#Reset for conditional probability
prob_time = time.time()

### Conditional Probabilities

#Given a login to a destination host, what's the probability of the src_nt_host being x?
df['p(src_nt_host|dest_nt_host)'] = df['p(src_nt_host n dest_nt_host)'] / df['p(dest_nt_host)']
df['p(dest_user|src_user)'] = df['p(src_user n dest_user)'] / df['p(src_user)']
df['p(dest_nt_host|dest_user)'] = df['p(dest_user n dest_nt_host)'] / df['p(dest_user)']

print("Conditional Probability time:")
print(time.time() - prob_time)

#Frequency of login
#TODO

print(df.head())

df.to_csv('auth_filtered_all_with_labels_sorted_2_with_labels.csv')

end_time = time.time()
print("Duration:")
print(end_time - start_time)
