from pathy import Path,Expand
home = Expand("~")

oldconfig = home(".gitconfig")
config = home(".config","git")
newconfig = config("config")
attributes = config("attributes")

if oldconfig.exists():
    if newconfig.exists():
        print("Warning! You have two config files. {} will be ignored while {} exists!".format(newconfig,oldconfig))
        config = oldconfig
    else:
        print("Should I move the old {} to {}?".format(oldconfig,newconfig))
        if input() == 'y':
            config.mkdir()
            oldconfig.rename(newconfig)
            print("Successfully moved")
            config = newconfig
        else:
            print("Keeping old config")
            config = oldconfig
else:
    config = newconfig

def upgrade(config,added):
        with open(added) as inp:
            added = inp.read()
        with open(config.expand()) as inp:
            oldconfig = inp.read()
            if added in oldconfig:
                print("Already set for {}".format(config))
                return
        print("^C if you don't want to add this to {}:\n{}".format(config,added))
        input()
        tmp = config.tail('.tmp')
        with open(tmp,'w') as out:
            out.write(oldconfig + '\n' + added)
        tmp.rename(config)

upgrade(config,"config")
upgrade(attributes,"attributes")

print("OK you're set.")
