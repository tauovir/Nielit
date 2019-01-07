from textblob.classifiers import NaiveBayesClassifier

def qa1():
    trainData = [
            ('Augmentation mentoplasty using Mersilene mesh.  Many different materials are available for augmentation mentoplasty.  However, the optimal implant material for chin implantation has yet to be found.  During the past several years, a number of experienced surgeons have turned to the use of Mersilene mesh.  Mersilene mesh is a non-absorbable Dacron polyester fiber that can be conformed easily into layers to achieve tailored dimensions and shape.  At the McCollough Plastic Surgery Clinic PA, Birmingham, Ala, 277 patients over a 10-year period underwent chin augmentation with Mersilene mesh implants.  The material provides excellent tensile strength, durability, and surgical adaptability.  The overall complication rate was 3.2% (nine patients); infection rate, 2.5% (seven patients); and removal secondary to infection, 1.7% (five patients).  Based on this 10-year experience, Mersilene mesh remains our material of choice for chin augmentation.','C01'),
            ('Multiple intracranial mucoceles associated with phaeohyphomycosis of the paranasal sinuses.  The purpose of this article is to alert clinicians to a new pathogenic fungus of the paranasal sinuses called Exserohilum rostratum.  Exserohilum species are one of the etiologic agents of phaeohyphomycosis, a constellation of entities caused by dematiaceous fungi.  This class of fungal sinus infection has emerged only in the past decade; it occurs primarily in immunocompetent individuals and produces a tenacious, progressive pansinusitis.  To our knowledge, this study describes the first case of multiple intracranial mucoceles secondary to E rostratum.  The diagnostic workup includes computed tomography and magnetic resonance imaging followed by direct microscopic examination of tissue biopsy specimens.  A craniotomy followed by a bilateral external ethmoidectomy was necessary for complete extirpation of the infected mucoceles.  Aggressive surgical management of this mycotic infection is described','C01'),
            ('Laser photodynamic therapy for papilloma viral lesions.  Photodynamic therapy was tested for its therapeutic efficacy in eradicating rabbit papilloma warts. The wild-type viral warts suspension was used to induce treatable papilloma warts in the cutaneous tissue of Dutch Belted rabbits. The photosensitizing agents used intravenously were Photofrin II at 10 mg/kg of body weight and Chlorin e6 monoethylene diamine monohydrochloric acid (Chlorin e6 med HCl) at 1 mg/kg of body weight.  The lasers used were an argon-dye laser at 628 and 655 nm and a gold vapor laser at 628 nm.   The irradiances of 25 to 180 mW/cm2 were applied topically with an end-on lens optical fiber with total radiant doses of 7.5 to 54 J/cm2.  Photofrin II and the argon-dye laser at the highest light dosage (54 J/cm2) and Chlorin e6 monoethylene diamine monohydrochloride administered 2 hours before argon-dye laser irradiation at 655 nm at the highest light dosage (54 J/cm2) produced wart regression.  Total wart regression without recurrence was achieved with Photofrin II and the gold vapor laser at all light dosages.  The difference observed between the argon-dye laser and the gold vapor laser might be explained by the pulsed nature of the gold vapor laser, with its high-peak powers, some 5000 x the average measured light dose.  In this model, the smaller, less cornified lesions were more effectively treated with photodynamic therapy.','C02'),
            ('Role of the monocyte-macrophage in influenza virus infection of lymphocytes: implications for HIV infection.  Knowledge of the pathogenesis of viruses which are less virulent than human immunodeficiency virus (HIV) may provide valuable insights into the pathogenesis of HIV infection.  Influenza virus, an enveloped RNA virus, infects monocyte-macrophages, although the infection is brief and abortive.  Isolated purified lymphocytes are completely resistant to infection.  In contrast, mixtures of lymphocytes and macrophages can synthesize all virus proteins.  Infection requires physical association of monocyte-macrophages and lymphocytes in "clusters." These studies with influenza virus suggest that the pathogenesis of virus infections in mixed cell cultures may be very different from that observed in purified cell populations, and they suggest that similar studies should be performed with HIV.','C01'),
            ('Use of polymerase chain reaction for successful identification of asymptomatic genital infection with herpes simplex virus in pregnant women at delivery.  The polymerase chain reaction was adapted to the amplification of a herpes simplex virus (HSV) DNA sequence, common to HSV types 1 and 2 (HSV-1, HSV-2).  The amplified product was detectable by ethidium-bromide staining or Southern hybridization of gels and by dot hybridization.  The HSV polymerase chain reaction detected HSV DNA in samples obtained from eight patients with genital lesions from which HSV-2 was isolated in tissue culture and from four patients with labial lesions from which HSV-1 was isolated.  The HSV polymerase chain reaction identified HSV in clinical specimens obtained from 11 women who had asymptomatic genital HSV infections at delivery.  None of 11 samples obtained at delivery from women who had antibodies to HSV-2, but whose delivery cultures were negative, were positive by polymerase chain reaction and no false-positive reactions were obtained when the reaction mixture contained human cell DNA or varicella-zoster virus, cytomegalovirus, Epstein-Barr virus, or human papillomavirus DNA.','C02')
            ]
    classifier = NaiveBayesClassifier(trainData)
    #str1 = "A school blood drive before a measles outbreak permitted correlation of preexposure measles antibody titers with clinical protection using the plaque reduction neutralization (PRN) test and an EIA."
   # print(classifier.classify(str1))
    testdata = [
            'A school blood drive before a measles outbreak permitted correlation of preexposure measles antibody titers with clinical protection using the plaque reduction neutralization (PRN) test and an EIA.',
            'Of 9 donors with detectable preexposure PRN titer less than or equal to 120, 8 met the clinical criteria for measles (7 seroconfirmed) compared with none of 71 with preexposure PRN titers greater than 120 (P less than .0001).',
            'Seven of 11 donors with preexposure PRN titers of 216-874 had a greater than or equal to 4-fold rise in antibody titer (mean, 43-fold) compared with none of 7 with a preexposure PRN titer greater than or equal to 1052 (P less than .02).',
            'Of 37 noncases with preexposure PRN titer less than 1052, 26 (70%) reported one or more symptoms compared with 11 (31%) of 35 donors with preexposure PRN titers greater than or equal to 1052 (P less than .002).',
            'By EIA, no case had detectable preexposure antibody; the preexposure geometric mean titer of asymptomatic donors (220) was not significantly higher than that of symptomatic donors who did not meet the clinical criteria for measles (153) (P = .10).',
            'The study suggests that PRN titers less than or equal to 120 were not protective against measles disease and illness without rash due to measles may occur in persons with PRN titers above this level.',
            'Use of polymerase chain reaction for successful identification of asymptomatic genital infection with herpes simplex virus in pregnant women at delivery.  The polymerase chain reaction was adapted to the amplification of a herpes simplex virus (HSV) DNA sequence, common to HSV types 1 and 2 (HSV-1, HSV-2).  The amplified product was detectable by ethidium-bromide staining or Southern hybridization of gels and by dot hybridization.  The HSV polymerase chain reaction detected HSV DNA in samples obtained from eight patients with genital lesions from which HSV-2 was isolated in tissue culture and from four patients with labial lesions from which HSV-1 was isolated.  The HSV polymerase chain reaction identified HSV in clinical specimens obtained from 11 women who had asymptomatic genital HSV infections at delivery.  None of 11 samples obtained at delivery from women who had antibodies to HSV-2, but whose delivery cultures were negative, were positive by polymerase chain reaction and no false-positive reactions were obtained when the reaction mixture contained human cell DNA or varicella-zoster virus, cytomegalovirus, Epstein-Barr virus, or human papillomavirus DN'
            ]
    for stmt in testdata:
        print(classifier.classify(stmt))

def qaTest():
    train = [
        ('I love this sandwich.', 'pos'),
        ('this is an amazing place!', 'pos'),
        ('I feel very good about these beers.', 'pos'),
        ('this is my best work.', 'pos'),
        ("what an awesome view", 'pos'),
        ('I do not like this restaurant', 'neg'),
        ('I am tired of this stuff.', 'neg'),
        ("I can't deal with this", 'neg'),
        ('he is my sworn enemy!', 'neg'),
        ('my boss is horrible.', 'neg')
        ]


    test = [
        ('the beer was good.', 'pos'),
        ('I do not enjoy my job', 'neg'),
        ("I ain't feeling dandy today.", 'neg'),
        ("I feel amazing!", 'pos'),
        ('Gary is a friend of mine.', 'pos'),
        ("I can't believe I'm doing this.", 'neg')
        ]
    cl = NaiveBayesClassifier(train)
    for stmt in test:
          print cl.classify(stmt[0])

#qa1()
qaTest()
