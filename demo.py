lt = ['\tUttar Pradesh\t265,270\t[1]', '02\tWest Bengal\t228,452\t[2]', '03\tMaharashtra\t220,458\t[3]', '04\tKarnataka\t207,332\t[4]', '05\tRajasthan\t166,766\t[5]', '06\tAndhra Pradesh\t159,025\t[6]', '07\tMadhya Pradesh\t142,452\t[7]', '08\tGujarat\t142,135\t[8]', '09\tBihar\t138,493\t[9]', '10\tTamil Nadu\t130,346\t[10]', '11\tOdisha\t103,350\t[11]', '12\tKerala\t101,140\t[12]', '13\tAssam\t90,194\t[13]', '14\tJharkhand\t50,110\t[14]', '15\tPunjab\t46,493\t[15]', '16\tChhattisgarh\t46,095\t[16]', '17\tHimachal Pradesh\t26,526\t[17]', '18\tUttarakhand\t25,959\t[18]', '19\tHaryana\t24,519\t[19]', '20\tTripura\t12,872\t[20]', '21\tDelhi\t8,249\t[21]', '22\tMeghalaya\t5,771\t[22]', '23\tGoa\t5,686\t[23]', '24\tManipur\t5,251\t[24]', '25\tMizoram\t3,154\t[25]', '26\tArunachal Pradesh\t2,363\t[26]', '27\tNagaland\t2,360\t[27]', '28\tPuducherry\t2,146\t[28]', '29\tAndaman and Nicobar Islands\t1,121\t[29]', '30\tSikkim\t1,049\t[30]', '31\tDaman and Diu\t477\t[31]', '32\tLakshadweep\t430\t[32]', '33\tChandigarh\t340\t[33]', '34\tJammu and Kashmir\t\t[34]', '35\tDadra and Nagar Haveli\t241\t[35]', '36\tLadakh ']
for i in lt:
    i = i.split('\t')[1]
    s = f'<option value="{i}">{i}</option>'
    print(s)