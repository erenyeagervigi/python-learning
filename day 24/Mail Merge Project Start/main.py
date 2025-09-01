
with open(r"C:\Users\Dell\Desktop\python learning\udemycourse\python pro course\day 24\Mail Merge Project Start\Input\Letters\starting_letter.txt") as file:
    contents = file.read()

with open(r"C:\Users\Dell\Desktop\python learning\udemycourse\python pro course\day 24\Mail Merge Project Start\Input\Names\invited_names.txt") as file1:
    contents1 = file1.readlines()

for name in contents1:
    names = name.strip()
    personal_invites = contents.replace("[name]", names)
    with open(rf"C:\Users\Dell\Desktop\python learning\udemycourse\python pro course\day 24\Mail Merge Project Start\Output\ReadyToSend\invitation_for_{names}.txt", "w") as file2:
        smtg = file2.write(personal_invites)

