current_users = ["pevilliarones", "papir", "odin", "loki", "p4pir", "gencer", "genco"] 
new_users = ["pevilliarones", "papir", "john", "mayer", "madden"]

for new_user in new_users:  
    if new_user in current_users:  
        print(f"{new_user} Bu isim kullanımda.")  
    else:  
        print(f"{new_user} Bu ismi kullanabilirsiniz.")  

registered_users = ["alice", "bob", "charlie", "david", "eve"]
applicants = ["bob", "frank", "george", "alice", "hannah"]
for applicant in applicants:
  if applicant in registered_users:
    print(f"{applicant} bu isim zaten kullanımda.")
  else:
    print(f"{applicant} bu ismi kullanabilirsiniz.")