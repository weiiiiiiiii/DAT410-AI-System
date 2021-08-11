import aiml,os
os.chdir('alice')
alice = aiml.Kernel()
alice.learn("startup.xml")
alice.respond('LOAD ALICE')

def tellAlice(str):
    res = alice.respond(str)
    print(res)

