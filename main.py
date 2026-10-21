
from pyscript import document


def candidate_checker(e):
    club_members = [
        'Tanjiro Kamado', 'Nezuko Kamado', 'Tanjuro Kamado',
        'Kie Kamado', 'Takeo Kamado', 'Hanako Kamado',
        'Shigeru Kamado', 'Rokuta Kamado', 'Sumiyoshi Kamado',
        'Suyako', 'Sumire', 'Zenitsu Agatsuma',
        'Inosuke Hashibira', 'Kotoha Hashibira', 'Aoba Hashibira',
        'Kanao Tsuyuri', 'Kanae Kocho', 'Shinobu Kocho',
        'Kiyoshi Kocho', 'Giyu Tomioka', 'Tsutako Tomioka',
        'Sabito', 'Makomo', 'Sakonji Urokodaki',
        'Kyojuro Rengoku', 'Shinjuro Rengoku', 'Ruka Rengoku',
        'Senjuro Rengoku', 'Tengen Uzui', 'Hinatsuru',
        'Makio', 'Suma', 'Mitsuri Kanroji', 'Obanai Iguro',
        'Sanemi Shinazugawa', 'Genya Shinazugawa',
        'Shizu Shinazugawa', 'Kyogo Shinazugawa',
        'Sumi Shinazugawa', 'Teiko Shinazugawa',
        'Hiroshi Shinazugawa', 'Koto Shinazugawa',
        'Shuya Shinazugawa', 'Muichiro Tokito',
        'Yuichiro Tokito', 'Gyomei Himejima',
        'Jigoro Kuwajima', 'Kaigaku', 'Yoriichi Tsugikuni',
        'Michikatsu Tsugikuni', 'Akeno Tsugikuni',
        'Masachika Kumeno', 'Murata', 'Aoi Kanzaki',
        'Sumi Nakahara', 'Kiyo Terauchi', 'Naho Takada',
        'Goto', 'Masao Maeda', 'Hotaru Haganezuka',
        'Kozo Kanamori', 'Tecchin Tecchikawahara',
        'Kotetsu', 'Tetsumotonaka', 'Tetsudoji', 'Tetsutani',
        'Tetsuido', 'Kagaya Ubuyashiki', 'Amane Ubuyashiki',
        'Hinaki Ubuyashiki', 'Nichika Ubuyashiki',
        'Kiriya Ubuyashiki', 'Kuina Ubuyashiki',
        'Kanata Ubuyashiki', 'Senri Ubuyashiki',
        'Akito Ubuyashiki', 'Kokushibo', 'Muzan Kibutsuji',
        'Tamayo', 'Yushiro', 'Chachamaru', 'Susamaru',
        'Yahaba', 'Temple Demon', 'Hand Demon',
        'Swamp Demon', 'Asakusa Demon', 'Tongue Demon',
        'Horned Demon', 'Spider Demon (Mother)',
        'Spider Demon (Father)', 'Spider Demon (Son)',
        'Spider Demon (Daughter)', 'Headless Demon',
        'Slasher', 'Mantis Demon', 'Woodland Demon',
        'Flute Demon', 'Serpent Demon', 'Hairo', 'Ubume',
        'Matazo', 'Rui', 'Kyogai', 'Enmu', 'Rokuro',
        'Wakuraba', 'Mukago', 'Kamanue', 'Akaza', 'Doma',
        'Gyokko', 'Hantengu', 'Sekido', 'Karaku', 'Aizetsu',
        'Urogi', 'Zohakuten', 'Urami', 'Gyutaro', 'Daki',
        'Nakime', 'Takaharu', 'Saburo', 'Kazumi', 'Satoko',
        'Tokie', 'Toyo', 'Rei', 'Yatsu', 'Koinatsu',
        'Omitsu', 'Kiyo', 'Sayo', 'Keizo', 'Koyuki',
        'Uta', 'Taro', 'Chuntaro', 'Kaburamaru', 'Yae',
        'Ozaki', 'Takeuchi', 'Nagakura', 'Noguchi',
        'Yoshioka', 'Shimamoto', 'Uraga',
        'Kanata Kamado', 'Sumihiko Kamado',
        'Toko Agatsuma', 'Yoshiteru Agatsuma',
        'Giichi Tomioka', 'Sanehiro Shinazugawa',
        'Tenma Uzui', 'Tojuro Rengoku'
    ]

    f_name = document.querySelector("#first_name").value.strip()
    l_name = document.querySelector("#last_name").value.strip()

    if not f_name and not l_name:
        document.querySelector("#result").textContent = (
            "Please enter a first name or a character name."
        )
        return

    candidate = f"{f_name} {l_name}".strip()
    member_names = {name.casefold() for name in club_members}

    if candidate.casefold() in member_names:
        message = (
            f"Congratulations, {candidate}! "
            "You are now part of Demon Slayer: Kimetsu No Yaiba!!"
        )
        result_color = "#753746"
        result_background = "#f5dce1"
    else:
        message = (
            f"Sorry, {candidate}, your name is not on the list. "
            "See you next season!"
        )
        result_color = "#826d72"
        result_background = "#fbf0f2"

    result = document.querySelector("#result")
    result.textContent = message
    result.style.color = result_color
    result.style.backgroundColor = result_background

