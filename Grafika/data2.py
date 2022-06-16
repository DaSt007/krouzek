states = {
    "1": {
        "name": "Začátek hry",
        "description": "Jestli cheš začít hru, napiš -jo- kdykoli to budeš chtít vzdát, napiš -x-.",
        "options": {
            "jo": {
                "target": "2",
                "description":
                    "Pak tedy vítej dobrodruhu!\n\n Strašný Gorgoth se dostal do čela barbarů, "
                    "unesl knížecí dceru a drží ji jako rukojmí, takže kníže nemuže pomoci králi v boji proti Gorgothovy. "
                    "Tvým úkolem je zachránit knížecí dceru."
            },
        }
    },
    "2": {
        "name": "seznámení s oklím",
        "description": "Po dvou dnech cesty jsi konečně dorazil na místo Gorgothova pobytu.\n Pod tebou je cesta pro Gorgothovy posly. Před tebou je Gogrothova věž, kterou původně postavili trpaslíci. Ti už tu ale nežijou.\n Ale co to? Najednou slyšíš na cestě kroky. Je to Gorgothův posel... Chceš na něj zaútočit-a-,\n nebo za ním tiše běžet a sledovat ho-b-\n nebo si chceš rozdělat ohníček a opéct si špekáček-c-? ",
        "options": {
            "c": {
                "target": "4",
                "description": "udělal sis špekáček, když vtom tě někdo praštil do hlavy..."
            },
            "a": {
                "target": "3",
                "description": "Vyskočil jsi na posla ze zálohy a ještě za letu jsi ho omráčil jílcem svého meče..."
            },
                        "b": {
                "target": "8",
                "description": "Tiše jsi za poslem běžel, dokud nedoběhl ke věži...\nDál jsi se musel plížit... doplížil jsi se na třicet metrů od brány, kam pávě posel přiběhl...\n Stráže posla zastavili, něco si říkají, ale ty je neslyšíš..."
            }
        },
    },
    "3": {
        "name": "výslech",
        "description": "Omráčeného posla jsi odtáhl do svého tábořiště a svázal jsi ho. Chceš počkat až se probere a vyslíchat ho-o-, nebo ho na místě zabít, obrat a zakopat v lese-f-?",
        "options": {
            "o": {
                "target": "5",
                "description":"Když se posel probral, spoustu ti toho vyžvanil. Tvrdil, že před odjezdem z tábora našel s kamarády ve skalách tajné dveře a okolo sochy trpaslíků, a že si myslí, že by mohla vést do opuštěného trpasličího města, a jelikož věž kterou teď obývá Gorgoth byla původně postavena trpaslíky, musí podle něj ústit nějaká tajná chodba až do věže...  " 
            },
            "f":{
                "target": "5",
                "description": ""
            
            },
            
        }
    },

     "4": {
        "name": "vězení a Gorgoth",
        "description": "Probudil ses druhý den ráno v barbarském vězení.\n Další den ráno tě předvedli před Gorgotha do věže. Povedlo se ti rozvázat si pouta tak, že si toho stráž nevšimla.\n Chceš se vrhnout na Gorgotha beze zbraně a pokusit se ho zabít holíma rukama-sos-, nebo se vrhnout na stráž a pokusit se jí holíma rukama zabít-lol-, nebo plivnout Gorgothovy do ksichtu-hrk-?",
        "options": {
            "lol": {
                "target": "123",
                "description": "Vhrl ses na stráž a povedlo se ti ji dokonce holýma rukama zabít, když tu ti Gorgoth rozmáčkl hlavu." 
            },
            "sos": {
                "target": "123",
                "description": "Vrhl ses na Gorgotha a ten tě rozsekl sekerou vedví. Poté ti dal navršit mohylu a na kámen dal vytesat: = sebevrah co se na mne vrhl= Gorgoth"
            },
            "hrk":{
                "target": "123",
                "description": " Gorgoth ti usekl hlavu, dal ji nabodnout na kůl a pod kůl dal umístit kovovou památní destičku s nápisem: =Takto dopadl chlap co se proslavil jen tím, že Gorgothovy plivl do ksichtu...="
            
            },
        }   
    },            
        "5": {
        "name": "zakopání v lese",
        "description": "Posla jsi zabil, obral, zakopal v lese a teď si prohlížíš jeho věci: Našel jsi u něj 25 zlatých, zapečetěnou ruličku papíru(asi zprávu a asi tajnou), a vzal jsi si také jeho šaty. Chceš si přečíst zprávu-p-, nebo si zprávou vytřít zadek-vy-, nebo použít zprávu na podpal a udělat si na ohni špekáček-š-?",
        "options": {
            "p": {
                "target": "6",
                "description":" Zpráva je skutečně adresovaná Gorgothovy a je od jakéhosi poručíka Moglara. Zní takto: Můj pane Gorgothe, tvůj rozkaz se mi podařilo splnit. V knihovnách jsme našly také zmínky o tom, že v  tomto kraji se skutečně nacházejí bohatá ložiska Galvornu. Zraky se ti rozšířili dychtivostí... Galvorn! Velice vzácný kov tvrdý jako trpasličí ocel a lehký jako mitrhil! Je také velice ohebný a dobře kujný... Tak proto je ve zdejším kraji tolik kráterů! Galvorn je přeci kov z vesmíru! muselo tu někdy v prvním věku spadnout mnoho asteroidů..." 
            },
            "vy":{
                "target": "4",
                "description": "Zrovna sis vytíral zadek, když tu tě někdo praštil do hlavy a omráčil tě..."
            
            },
            "š":{
                "target": "4",
                "description": "Zrovna jsi hodoval na špekáčku, když tu tě někdo praštil do hlavy a omráčil tě..."
            
            },
        }
    },
   "123": {
        "name": "Smrt",
        "description": "Chcípls, zhebnuls, zdechnuls, atd. Zkrátka jsi po smrti... stiskni -x- pro ukončení, -r- pro restart...", 
        "options": {
            "r": {
                "target": "1",
                "description":"Restart..." 
            },
        }
   },
   "6": {
        "name": "Tábor",
        "description": 
            "Nyní jsi tedy oblečen do nepřátelské uniformy. Takto "
            "oděn můžeš se pokusiti projít nepřátelským táborem. Chceš "
            "se o to pokusit-nepř-, nebo běžet po cestě až ke věži-věž-, nebo se jít vyčůrat do lesa-vyč-?",
        "options": {
            "vyč": {
                "target": "4",
                "description":"Zrovna jsi močil, když tu tě někdo omráčil klackem..." 
            },
            "nepř":{
                "target": "7",
                "description": "Když jsi procházel nepřátelským táborem, zavolal na tebe hrozně sklíčeně a opile vypadající Barbar: Hej! Pomůžeš mi utopit žal v alkoholu?"
            
            },
            "věž":{
                "target": "4",
                "description": "Došel jsi až ke věži. U vysokých schodů jsou dva ztrážní... Jeden se tě zeptá: Máš zprávu? Pak ale druhý: Zpráva potom, teď ukaž tetování, znak toho, že jsi na naší straně! Poté ti odhrne rukáv, zařve: Ha! A druhý tě omráčí sekerou..."
            
            }, 
        }
   },
      "7": {
        "name": "Pitka",
        "description": "Chceš odpovědět ano-ano- a jít se s ním napít, nebo říct že nemáš čas a pokračovat směrem ke věži-pokr-, nebo si jít odpočinout na skálu za táborem-skál-?",
        "options": {
            "ano": {
                "target": "9",
                "description":"Přišli jste do stanu, který nejspíš slouží jako bar... Opilec se slovy: Nalej Chlast! hodil na stůl zlaťák... Jeho vyprávění se teď už asi nevyhneš... Opilec si naleje a spustí: Víš, co se stalo? Troga odsoudili k smrti!(vyprázdnil jedním hltem svůj korbel...) a to jenom proto, že si šel s kamarády zalovit do skal a něco tam našel!(taky jsi se napil, je to streašně silné a pálí to, jestli chceš zůstat při smyslech tak toho vypij co nejmíň...) Taková nespravedlnost! Ještě než o tom podal hlášení a co si ho zavolali o tom se mnou mluvil... Tvrdil že ve skalách našel vchod do ňáký tý opuštěný trpajzličí štoly... Schylovalo se k bouři, takže se rozhodli tam přečkat noc...(objednal další alkohol...) A Druhý den ráno jim chyběl jeden kamarád! Proihledali okolí, a pak se s několika pochodněma odvážili do jeskyně... Šli sotva pár minut, když narazili na tělo jejich mrtvýho kamaráda!! Někdo mu prosekl hrdlo!! U sebe měl tasený meč potřísněnej krví... Ale nejdivnější bylo, že když ho vohledali z blízka vypadal jako by ho někdo prohledal... (je tak ponořený do vyprávění že už zapoměl i chlastat...) A pak to oběvili! Kapky krve na zemi, jako když odchází ráněný z bojiště, se táhly dál do podzemí... Víc mi toho neřek, zavolal si ho totiž poručík aby mu podal hlášení. Dva dny nato ho popravili... Divný, co? " 
            },
            "skál":{
                "target": "11",
                "description": "Došel jsi ke skalám za táborem, o kousek dál byla stěna kráteru ve kterém jsi se nacházel... došel jsi k malému potůčku, když tu jsi zakopl o kámen... S klením jsi se zvedl a podíval se na toho mizeru, když tu ti došlo, co to vlastně je... Zakopl jsi o nějaký kamenný ukazatel! a na něm trpasličí runy! klekneš si k nim a přečteš je: Berúm Khazad ol norden... v překladu: Trpasličí brána na sever..."
            
            },
                        "pokr":{
                "target": "4",
                "description": "Došel jsi až ke věži. U vysokých schodů jsou dva ztrážní... Jeden se tě zeptá: Máš zprávu? Pak ale druhý: Zpráva potom, teď ukaž tetování, znak toho, že jsi na naší straně! Poté ti odhrne rukáv, zařve: Ha! A druhý tě omráčí sekerou..."
            
            }, 
        }
   },
   "9": {
        "name": "",
        "description": 
            "Chceš vyrazit na skály za táborem a pátrat po té štole-j-,\n nebo pokračovat ke věži-fo-\n nebo se opít-opít-?",
        "options": {
            "j": {
                "target": "11",
                "description":"Došel jsi na skály za táborem, když tu jsi zakopl o ukazatel. Na ukazateli je napsáno Trpasličí brána na sever..." 
            },
            "opít":{
                "target": "123",
                "description": "upil jsi se k smrti..."
            
            },
            "fo":{
                "target": "4",
                "description": "Došel jsi až ke věži. U vysokých schodů jsou dva ztrážní... Jeden se tě zeptá: Máš zprávu? Pak ale druhý: Zpráva potom, teď ukaž tetování, znak toho, že jsi na naší straně! Poté ti odhrne rukáv, zařve: Ha! A druhý tě omráčí sekerou..."
            
            }, 
        }
   },

        "8": {
        "name": "Odpslouchávání",
        "description": "Chceš se k nim připlížit o pět metrů-5-, nebo se k nim připlížit o deset metrů-10-, nebo si udělat špekáček-špek-?",
        "options": {
            "10": {
                "target": "4",
                "description":"Když ses plížil, všiml si tě jeden strážný... \npěti skoky byl u tebe a omráčil tě sekerou..." 
            },
            "5":{
                "target": "10",
                "description": "připlížil jsi se na patnáct metrů od stráží... jeden právě říka ostatním:\n Tak jo, půjdu to odevzdat šéfovi, ale bude to trvat tak hodinu, možná dvě, takže tu zůstaň, Bjork tu mezitím s tebou zůstane...\n Poté odejde po dlouhých schodech nahoru ke vratům věže... pět minut nato Bjork navrhne poslovi že si půjdou sednout dovnitř do strážnice k lahvi něčeho na zahřátí, protože se cítí prokřehlý\n Následně oba odejdou... připlížil jsi se k okýnku do strážnice... po deseti minutách, zmoženi silnou kořalkou, už oba spali..."
            
            },
            "špek":{
                "target": "4",
                "description": "Zrovna jsi se postavil, abys našel místo na ohniště, když tu si tě stráže všimly, přiběhly k tobě a omráčili tě sekerou..."
            
            }, 
        }
   },
        "10": {
        "name": "Odpslouchávání",
        "description": "Teď když oba spí, můžeš se pokusiti vyběhnouti schody až ke dveřím věže-běh-,\n nebo chceš radši zpátky do svého tábořiště-sůl-,\n nebo si chceš radši opéct špekáček-špekáček-?",
        "options": {
            "běh": {
                "target": "123",
                "description":"v půlce schodů jsi šlápl na jeden schod, ten spustil past, ze stěny vyletěla šipka a zabila tě..." 
            },
            "sůl":{
                "target": "4",
                "description": "došel jsi do svého tábořiště, když tu tě někdo praštil do hlavy..."
            
            },
            "špekáček":{
                "target": "13",
                "description": "Když jsi hledal místo na ohniště, propadla se pod tebou země... Upadl jsi do bezvědomí, když ses vzbudil, zjistil jsi že jsi v úplné tmě... rozsvítil jsi lucernu..."
            
            }, 
        }
   },
        "13": {
        "name": "na prahu",
        "description": "Světlo tvé lucerny zahnalo tmu. Zřítil jsi se do nějaké podzemní chodby. \nPět metrů nad tebou je otvor, kterým jsi se propadl. \nza tebou je chodba zavalena. \npřed tebou jsou dveře. \nnalevo ústí dalšií chodba. \nChceš vylézt otvorem nahoru-nah-,\n nebo se vydat chodbou vlevo-vlev-,\n nebo prozkomat dveře-dvere-?",
        "options": {
            "nah": {
                "target": "4",
                "description":"sotva jsi vylezl a napřímil se, někdo tě praštil do hlavy..." 
            },
            "vlev":{
                "target": "123",
                "description": "šel jsi chodbou asi pět metrů, pak jsi šlápl na past, ze stěny vyletělo ostří a zabilo tě..."
            
            },
            "dvere":{
                "target": "14",
                "description": "dveře jso kamené a nejdou otevřít. je na nich nápis v trpasličí řeči: Kdož vejít chcete, dejte pozor! Neumřete! Kdož správně zodpoví, dveře ho pustí... Kdož však chybu udělá, ten se strachy podělá... smrt ho stihne náhlesa"
            
            }, 
        }
   },


}
