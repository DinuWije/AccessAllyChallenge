OnegAvail, OposAvail, AnegAvail, AposAvail, BnegAvail, BposAvail, ABnegAvail, ABposAvail = map(
    int, input().split())
OnegPat, OposPat, AnegPat, AposPat, BnegPat, BposPat, ABnegPat, ABposPat = map(
    int, input().split())

available = {
    "Oneg": OnegAvail, "Opos": OposAvail, "Aneg": AnegAvail, "Apos": AposAvail,
    "Bneg": BnegAvail, "Bpos": BposAvail, "ABneg": ABnegAvail, "ABpos": ABposAvail
}

patients = {
    "Oneg": OnegPat, "Opos": OposPat, "Aneg": AnegPat, "Apos": AposPat,
    "Bneg": BnegPat, "Bpos": BposPat, "ABneg": ABnegPat, "ABpos": ABposPat
}

treated = 0


def useONeg(patientType, treated):
    import pdb; pdb.set_trace()
    if available["Oneg"] < patients[patientType]:
        treated += available["Oneg"]
        patients[patientType] -= available["Oneg"]
        available["Oneg"] = 0
    else:
        treated += patients[patientType]
        available["Oneg"] -= patients[patientType]
        patients[patientType] = 0
    print("Oneg: {treated}".format(treated=treated))
    return treated


def useOPos(patientType, treated):
    if available["Opos"] == patients[patientType]:
        treated += available["Opos"]
        available["Opos"] = 0
        patients[patientType] = 0
    elif available["Opos"] < patients[patientType]:
        treated += available["Opos"]
        patients[patientType] -= available["Opos"]
        available["Opos"] = 0
        treated = useONeg(patientType, treated)
    else:
        treated += patients[patientType]
        available["Opos"] -= patients[patientType]
        patients[patientType] = 0
    print("Opos: {treated}".format(treated=treated))
    return treated


def useANeg(patientType, treated):
    if available["Aneg"] < patients[patientType]:
        treated += available["Aneg"]
        patients[patientType] -= available["Aneg"]
        available["Aneg"] = 0
    else:
        treated += patients[patientType]
        available["Aneg"] = 0
        patients[patientType] = 0
    print("Aneg: {treated}".format(treated=treated))
    return treated


def useAPos(patientType, treated):
    if available["Apos"] < patients[patientType]:
        treated += available["Apos"]
        patients[patientType] -= available["Apos"]
        available["Apos"] = 0
        treated = useANeg(patientType, treated)
        if patients[patientType] != 0:
            treated = useOPos(patientType, treated)
    else:
        treated += patients[patientType]
        available["Apos"] -= patients[patientType]
        patients[patientType] = 0
    print("Apos: {treated}".format(treated=treated))
    return treated


def useBNeg(patientType, treated):
    if available["Bneg"] < patients[patientType]:
        treated += available["Bneg"]
        patients[patientType] -= available["Bneg"]
        available["Bneg"] = 0

    else:
        treated += patients[patientType]
        available["Bneg"] = 0
        patients[patientType] = 0
    print("Bneg: {treated}".format(treated=treated))
    return treated


def useBPos(patientType, treated):
    if available["Bpos"] < patients[patientType]:
        treated += available["Bpos"]
        patients[patientType] -= available["Bpos"]
        available["Bpos"] = 0
        treated = useBNeg(patientType, treated)
        if patients[patientType] != 0:
            treated = useOPos(patientType, treated)
    else:
        treated += patients[patientType]
        available["Bpos"] -= patients[patientType]
        patients[patientType] = 0
    print("Bpos: {treated}".format(treated=treated))
    return treated


def useABNeg(patientType, treated):
    if available["ABneg"] < patients[patientType]:
        treated += available["ABneg"]
        patients[patientType] -= available["ABneg"]
        available["ABneg"] = 0
        treated = useBNeg(patientType, treated)
        print("HERE1: {treated}".format(treated=treated))
        if patients[patientType] != 0:
            treated = useANeg(patientType, treated)
            print("HERE2: {treated}".format(treated=treated))
    else:
        treated += patients[patientType]
        available["ABneg"] -= patients[patientType]
        patients[patientType] = 0
    print("ABneg: {treated}".format(treated=treated))
    return treated


def useABPos(treated):
    if available["ABpos"] < patients["ABpos"]:
        treated += available["ABpos"]
        patients["ABpos"] -= available["ABpos"]
        available["ABpos"] = 0
        treated = useABNeg("ABpos", treated)
        if patients["ABpos"] != 0:
            treated = useBPos("ABpos", treated)
        if patients["ABpos"] != 0:
            treated = useAPos("ABpos", treated)
    else:
        treated += patients["ABpos"]
        available["ABpos"] -= patients["ABpos"]
        patients["ABpos"] = 0
    print("ABpos: {treated}".format(treated=treated))
    return treated


if __name__ == '__main__':
    treated = useONeg("Oneg", treated)
    treated = useOPos("Opos", treated)
    treated = useANeg("Aneg", treated)
    if patients["Aneg"] != 0:
        treated = useONeg("Aneg", treated)
    treated = useAPos("Apos", treated)
    treated = useBNeg("Bneg", treated)
    if patients["Bneg"] != 0:
        treated = useONeg("Bneg", treated)
    treated = useBPos("Bpos", treated)
    # print(available["Oneg"])
    # print(available["Opos"])
    # print(available["Aneg"])
    # print(available["Apos"])
    # print(available["Bneg"])
    # print(available["Bpos"])
    # print(available["ABneg"])
    # print(available["ABpos"])
    treated = useABNeg("ABneg", treated)
    if patients["ABneg"] != 0:
        treated = useONeg("ABneg", treated)
    treated = useABPos(treated)

    print(treated)


# def useAOrBPos(patientType, treated):
#     if available[patientType] < patients[patientType]:
#         treated += available[patientType]
#         patients[patientType] -= available[patientType]
#         available[patientType] = 0
#         treated = useAorBNeg(patientType, treated, None)
#         if patients[patientType] != 0:
#             treated = useOPos(patientType, treated)
#         return treated
#     else:
#         treated += patients[patientType]
#         available[patientType] -= patients[patientType]
#         patients[patientType] = 0
#         return treated
