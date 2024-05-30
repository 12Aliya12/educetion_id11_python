def number_in_english(number):
    resultat = []
    if not number:
        print('zero')
    else:
        do_desyati = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
        sd, e = divmod(number, 10)
        s, d = divmod(sd, 10)

        if s:
            resultat.append(do_desyati[s-1] + 'hundred')
        if d == 1:
            resultat.append(('ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
                    'sixteen', 'seventeen', 'eighteen', 'nineteen')[e])
        else:
            if d > 1:
                resultat.append(('twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty',
                        'ninety')[d-2])
            if e:
                resultat.append(do_desyati[e-1])
        print(*resultat)


number = int(input())
number_in_english(number)