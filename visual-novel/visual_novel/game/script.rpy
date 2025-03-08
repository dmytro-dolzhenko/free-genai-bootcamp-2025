init:
    define alex = Character("Alex", color="#5DADE2", image="alex")
    define hana = Character("Hana", color="#E74C3C", image="hana")
    define kaito = Character("Kaito", color="#F1C40F", image="kaito")
    define yuki = Character("Yuki", color="#9B59B6", image="yuki")

    # Relationship tracking variables
    default hana_affection = 0
    default kaito_affection = 0

    # Sound files
    define sound_alex_intro = "transcripts/alex_intro.mp3"
    define sound_hana_intro = "transcripts/hana_intro.mp3"
    define sound_alex_formal_greeting = "transcripts/alex_formal_greeting.mp3"
    define sound_hana_response = "transcripts/hana_response.mp3"
    define sound_alex_casual_greeting = "transcripts/alex_casual_greeting.mp3"
    define sound_hana_casual_response = "transcripts/hana_casual_response.mp3"
    define sound_alex_first_class = "transcripts/alex_first_class.mp3"
    define sound_kaito_intro = "transcripts/kaito_intro.mp3"
    define sound_alex_thought = "transcripts/alex_thought.mp3"
    define sound_alex_ask_book = "transcripts/alex_ask_book.mp3"
    define sound_kaito_book_response = "transcripts/kaito_book_response.mp3"
    define sound_alex_compliment_attire = "transcripts/alex_compliment_attire.mp3"
    define sound_kaito_attire_response = "transcripts/kaito_attire_response.mp3"
    define sound_hana_shibuya = "transcripts/hana_shibuya.mp3"
    define sound_hana_tea_shop = "transcripts/hana_tea_shop.mp3"
    define sound_hana_music_store = "transcripts/hana_music_store.mp3"
    define sound_hana_music_store_response = "transcripts/hana_music_store_response.mp3"
    define sound_kaito_tea_shop_response = "transcripts/kaito_tea_shop_response.mp3"
    define sound_yuki_ryokan = "transcripts/yuki_ryokan.mp3"
    define sound_hana_tea_ceremony = "transcripts/hana_tea_ceremony.mp3"
    define sound_kaito_calligraphy = "transcripts/kaito_calligraphy.mp3"
    define sound_hana_volunteers = "transcripts/hana_volunteers.mp3"
    define sound_kaito_literature_club = "transcripts/kaito_literature_club.mp3"
    define sound_hana_music_club_response = "transcripts/hana_music_club_response.mp3"
    define sound_kaito_literature_club_response = "transcripts/kaito_literature_club_response.mp3"
    define sound_hana_festival_success = "transcripts/hana_festival_success.mp3"
    define sound_kaito_show_something = "transcripts/kaito_show_something.mp3"
    define sound_hana_fireworks = "transcripts/hana_fireworks.mp3"
    define sound_kaito_haiku = "transcripts/kaito_haiku.mp3"
    define sound_alex_decision = "transcripts/alex_decision.mp3"
    define sound_alex_return_home = "transcripts/alex_return_home.mp3"
    define sound_hana_farewell = "transcripts/hana_farewell.mp3"
    define sound_kaito_farewell = "transcripts/kaito_farewell.mp3"
    define sound_yuki_farewell = "transcripts/yuki_farewell.mp3"
    define sound_alex_farewell_response = "transcripts/alex_farewell_response.mp3"
    define sound_alex_stay_decision = "transcripts/alex_stay_decision.mp3"
    define sound_hana_stay_response = "transcripts/hana_stay_response.mp3"
    define sound_kaito_stay_response = "transcripts/kaito_stay_response.mp3"
    define sound_yuki_stay_response = "transcripts/yuki_stay_response.mp3"
    define sound_alex_stay_response = "transcripts/alex_stay_response.mp3"

    # Add the following lines to define the images for each character
    image alex = im.FactorScale("images/characters/alex.png", 0.8)
    image hana = im.FactorScale("images/characters/hana.png", 0.8)
    image kaito = im.FactorScale("images/characters/kaito.png", 0.8)
    image yuki = im.FactorScale("images/characters/yuki.png", 0.8)

    image school = "images/places/school.png"
    image classroom = "images/places/classroom.png"
    image shibuya = "images/places/shibuya.png"
    image ryokan = "images/places/ryokan.png"
    image school_festival = "images/places/school_festival.png"
    image festival_night = "images/places/festival_night.png"
    image decision_point = "images/places/decision_point.png"

    # Define a custom position between left and center
    transform left_center:
        xalign 0.25  # Adjust this value to position between left and center

    transform center_right:
        xalign 0.75  # Adjust this value to position between center and right

label start:
    scene school with fade

    show alex at left
    play sound sound_alex_intro
    alex "Wow, so this is Sakura High School. My new beginning in Japan. (わあ、ここが桜高校か。日本での新しい始まりだ。)"
    
    show hana at right
    play sound sound_hana_intro
    hana "Hello! You must be Alex. I'm Hana Sato, your guide. Welcome to our school! (こんにちは！あなたがアレックスですね。私は案内役の佐藤花です。学校へようこそ！)"
    
    menu:
        "(Option A) Greet formally in Japanese (日本語で丁寧に挨拶する)":
            $ hana_affection += 1
            play sound sound_alex_formal_greeting
            alex "It's an honor to meet you, Hana-san. I look forward to learning here. (花さん、お会いできて光栄です。ここで学ぶのを楽しみにしています。)"
            play sound sound_hana_response
            hana "Oh! You speak Japanese? That's wonderful! (えっ、日本語を話せるの？すごい！)"
        "(Option B) Greet casually in English (英語でカジュアルに挨拶する)":
            play sound sound_alex_casual_greeting
            alex "Hey! Nice to meet you, Hana! (やあ！花、会えてうれしいよ！)"
            play sound sound_hana_casual_response
            hana "Nice to meet you too! I hope you'll enjoy your time here. (こちらこそ！ここでの時間を楽しんでね。)"

    scene classroom with fade
    show alex at right
    play sound sound_alex_first_class
    alex "My first class... (初めての授業...)"
    
    show kaito at left
    play sound sound_kaito_intro
    kaito "Oh, a new face. Are you the transfer student? (あ、新しい顔だね。君が転校生？)"
    play sound sound_alex_thought
    alex "(That guy looks interesting. Should I talk to him?) (あの人、面白そうだな。話しかけるべき？)"
    
    menu:
        "(Option A) Ask about his book (本について尋ねる)":
            $ kaito_affection += 1
            play sound sound_alex_ask_book
            alex "That book looks fascinating. What's it about? (その本、面白そうだね。何について書かれているの？)"
            play sound sound_kaito_book_response
            kaito "It's about ancient poetry. Not sure if you'd be interested. (これは古代の詩についての本だ。興味あるかな？)"
        "(Option B) Compliment his traditional attire (彼の伝統的な服装を褒める)":
            $ kaito_affection += 1
            play sound sound_alex_compliment_attire
            alex "Your outfit is really cool. Traditional, right? (その服、すごくかっこいいね。伝統的なもの？)"
            play sound sound_kaito_attire_response
            kaito "Oh... thanks. Not many notice. (ああ…ありがとう。あまり気づかれることはないけど。)"

    scene shibuya with fade
    show hana at right
    play sound sound_hana_shibuya
    hana "Hey, Alex! Want to explore Shibuya with me? (ねえ、アレックス！渋谷を一緒に探検しない？)"
    if kaito_affection > hana_affection:
        play sound sound_hana_tea_shop
        hana "Oh, I bet Kaito would love the traditional tea shop. Want to check it out? (カイトはきっと伝統的なお茶屋さんが好きだと思うな。一緒に行ってみない？)"
    else:
        play sound sound_hana_music_store
        hana "There's an amazing music store here! Want to go? (ここにすごい音楽ショップがあるよ！行ってみる？)"
    
    menu:
        "(Option A) Visit the music store (音楽ショップを訪れる)":
            $ hana_affection += 1
            play sound sound_hana_music_store_response
            hana "Awesome! Let's check out some records. (やった！レコードを見てみよう！)"
        "(Option B) Explore the traditional tea shop (伝統的なお茶屋を探索する)":
            $ kaito_affection += 1
            show kaito at left
            play sound sound_kaito_tea_shop_response
            kaito "I never expected you'd enjoy this. This tea is special. (君がこれを楽しむとは思わなかった。このお茶は特別だよ。)"
    
    scene ryokan with fade
    show yuki at left
    play sound sound_yuki_ryokan
    yuki "Welcome to my ryokan! We have a tea ceremony and calligraphy session. (私の旅館へようこそ！茶道と書道の体験ができますよ。)"
    menu:
        "(Option A) Tea ceremony (茶道を体験する)":
            $ hana_affection += 1
            show hana at right
            play sound sound_hana_tea_ceremony
            hana "I'll guide you through it. It's all about mindfulness. (私が案内するね。これは心を落ち着ける大切な文化なの。)"
        "(Option B) Calligraphy (書道を体験する)":
            $ kaito_affection += 1
            show kaito at right
            play sound sound_kaito_calligraphy
            kaito "I can teach you. It's a calming practice. (僕が教えるよ。心が落ち着く素晴らしい体験だよ。)"
    
    scene school_festival with fade
    show hana at right
    play sound sound_hana_volunteers
    hana "We need volunteers! Join my music club? (ボランティアを募集中！私の音楽部に入らない？)"
    show kaito at left
    play sound sound_kaito_literature_club
    kaito "The literature club could use help too. (文学部も助けが必要だ。)"
    menu:
        "(Option A) Music club (音楽部に参加する)":
            $ hana_affection += 1
            play sound sound_hana_music_club_response
            hana "I knew you'd choose us! Let's perform together. (選んでくれると思ってた！一緒に演奏しよう！)"
        "(Option B) Literature club (文学部に参加する)":
            $ kaito_affection += 1
            play sound sound_kaito_literature_club_response
            kaito "Great choice. Let's work on a special poem for the festival. (素晴らしい選択だ。文化祭のために特別な詩を作ろう。)"
    
    scene festival_night with fade
    show hana at right
    play sound sound_hana_festival_success
    hana "The festival was a success! Want to hang out? (文化祭、大成功だったね！少し遊ばない？)"
    show kaito at left
    play sound sound_kaito_show_something
    kaito "I have something to show you, Alex. (アレックス、見せたいものがあるんだ。)"
    menu:
        "(Option A) Spend time with Hana (花と過ごす)":
            $ hana_affection += 2
            play sound sound_hana_fireworks
            hana "Let's watch the fireworks together. (一緒に花火を見よう。)"
        "(Option B) Spend time with Kaito (カイトと過ごす)":
            $ kaito_affection += 2
            play sound sound_kaito_haiku
            kaito "I wrote something for you... a haiku about friendship. (君のために詩を書いたよ…友情の俳句だ。)"
    
    scene decision_point with fade
    show alex at center
    play sound sound_alex_decision
    alex "I need to decide... should I stay or go? (決めなきゃ…帰るべきか、残るべきか？)"
    menu:
        "(Option A) Return home (帰国する)":
            jump ending_home
        "(Option B) Extend stay (滞在を延長する)":
            jump ending_stay

label ending_home:
    scene airport with fade
    show alex at center_right
    play sound sound_alex_return_home
    alex "It's time to go back home. (帰る時が来た。)"
    show hana at right
    play sound sound_hana_farewell
    hana "We'll miss you, Alex. Stay in touch, okay? (寂しくなるね、アレックス。連絡してね？)"
    show kaito at left_center
    play sound sound_kaito_farewell
    kaito "Take care, Alex. I hope we meet again someday. (元気でね、アレックス。また会えるといいな。)"
    show yuki at left
    play sound sound_yuki_farewell
    yuki "Safe travels, Alex. Remember, you always have a place here. (気をつけてね、アレックス。ここはいつでも君の居場所だよ。)"
    play sound sound_alex_farewell_response
    alex "Thank you all for everything. I'll never forget my time here. (みんな、本当にありがとう。ここでの時間は忘れないよ。)"
    return

label ending_stay:
    scene celebration with fade
    show alex at left_center
    play sound sound_alex_stay_decision
    alex "I've decided to stay longer. There's so much more to experience. (もっと滞在することに決めた。まだまだ経験したいことがたくさんある。)"
    show hana at left
    play sound sound_hana_stay_response
    hana "That's wonderful! We'll make so many more memories together. (素晴らしい！もっとたくさんの思い出を作ろうね。)"
    show kaito at center_right
    play sound sound_kaito_stay_response
    kaito "I'm glad you're staying. Let's explore more of what Japan has to offer. (残ってくれて嬉しいよ。日本の魅力をもっと探検しよう。)"
    show yuki at right
    play sound sound_yuki_stay_response
    yuki "Welcome to your extended family, Alex. (アレックス、私たちの家族へようこそ。)"
    play sound sound_alex_stay_response
    alex "I'm looking forward to every moment. Thank you for welcoming me. (これからの時間が楽しみだよ。迎えてくれてありがとう。)"
    return
