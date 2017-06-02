def fixedeval(theinput):
    #takes a string and preps 'naked' alphanumeric chars as strings:
    fixed = theinput
    i = 0
    for x in fixed:
    #for i in range(0,len(fixed)):
        #x = fixed[i]
        #if it's not a number, assume character:
        g = i
        maxlength = 0
        y = fixed[g+1]
        if str(x) != "\"" and str(x) != "[" and str(x) != "]" and str(x) != ",":
            #1: figure out the length of alphas:
            while str(y) != "\"" and str(y) != "[" and str(y) != "]" and str(y) != ",":
                maxlength += 1
                if g+1 < len(fixed):
                    y = fixed[g+1]
                g += 1
            try:
                int(x)
            except(NameError,ValueError):
                if maxlength > 0:
                    FASTLANE = fixed[i:i+maxlength]
                    TAKEITSLOW = fixed[i+maxlength:]
                else:
                    FASTLANE = FASTLANE = fixed[i]
                    TAKEITSLOW = fixed[i+maxlength+1:]
                fixed = fixed[:i] + "\"" + FASTLANE + "\"" + TAKEITSLOW
                if maxlength > 0:
                    i += 2 + maxlength
                else:
                    i += 2
        i += 1
        try:
            fixed[i]
        except(IndexError):
            return eval(fixed)
    return eval(fixed)





fixed = "[c,[t,[a],[t]],cat]"
print("OG")
print(fixed)
#print(fixed[:3])
#print(fixed[3:])
print(fixedeval(fixed)[2])
