# 1001-tracklists-to-Youtube-Comment

This is a Python script that scrapes tracklists from 1001-tracklist.com and converts them into formatted YouTube comments.

The script requests the HTML code of a given tracklist URL, extracts the song titles and artists from the source code, and formats them into a comment-ready string for YouTube with timestamps included. The resulting string can be copied and pasted directly as a comment on a specific YouTube video.

The scraping is done with [Selenium](https://pypi.org/project/selenium/).
## Usage

```python
url = "https://1001.tl/rn1qu9t"         
try:
    formatter = TracklistFormatter(timeout=10)  # Increase timeout if needed
    formatted_comment = formatter.tracklist1001_url_to_youtube_comment(url)
    print(formatted_comment)
except Exception as e:
    print(f"Error: {str(e)}")

# The Output will look something like this:
"""
0:00 Damn Kids - Anxiety MAIN COURSE
1:00 w/ Bossfight - Warp MONSTERCAT
1:31 w/ Knock2 - dashstar* (VIP) NIGHT MODE
2:00 Gammer - The Drop (Stonebank Remix) MONSTERCAT
2:45 w/ Kill Feed - Back N' Forth (VIP!) NSD: BLACK LABEL
3:20 NGHTMRE & Ray Volpe - Signal GUD VIBRATIONS
4:40 Excision & Space Laces - Throwin' Elbows (Ricky West Flip) ROTTUN
   w/ JAUZ & Nonsens - The Beat BITE THIS!
6:25 JAUZ & Ephwurd - Rock The Party SPINNIN'
7:35 Space Laces - Dominate NEVER SAY DIE
8:24 JAUZ & Crankdat ft. Slushii - I Hold Still SELF RELEASED
9:35 Virtual Riot - Fork Funeral DISCIPLE
10:00 Valentino Khan & NITTI - Your Body SPINNIN'
10:35 NGHTMRE ft. A$AP Ferg - REDLIGHT (VIP) ULTRA
12:40 Knock2 - JADE SABLE VALLEY
13:20 Sebastian Ingrosso & Tommy Trash & John Martin vs. Nanoo - Poison Reload (Subshock & Evangelos Edit)
15:08 Fatboy Slim - Gangster Trippin (Sultan + Shepard Remix) ARMADA/SKINT
15:08 w/ 'N Sync - I Want You Back RCA (SONY)
   w/ ID - ID
16:30 Far Too Loud - Start The Party FUNKATECH
16:51 w/ Skrillex & Habstrakt - Chicken Soup OWSLA
17:02 w/ Kill Feed - Forsaken NEVER SAY DIE
17:24 NGHTMRE & Knock2 - ID
18:45 EPROM & G Jones - Hysteria ILLUSORY
19:50 Sullivan King & Subtronics - Take Flight CYCLOPS
20:35 ISOxo - REDloop SABLE VALLEY
21:40 JAUZ & KAYZO - ID
23:00 JAUZ & Lazer Lazer Lazer - Keep The Rave Alive (Intro Edit) BITE THIS!
   w/ Skrillex & Kill The Noise ft. Fatman Scoop & Michael Angelakos - Recess (Acappella) OWSLA/BIG BEAT
25:00 Benny Benassi pres. The Biz - Satisfaction (Cheyenne Giles Flip) FREE
   w/ Skrillex & MUST DIE! - VIP's (Acappella) OWSLA
   w/ Eptic & MARAUDA - Wall Of Death OVERLORD
26:20 Post Malone ft. Quavo - Congratulations (Dzeko Remix) FREE/REPUBLIC
   w/ Kaaris - Chargé (Mr. Carmack Remix / Boombox Cartel Remix / ISOxo Edit) DEF JAM
27:50 Datsik & Virtual Riot - Nasty (ID Remix) FIREPOWER
   w/ ETC!ETC! & Brillz - Swoop MAD DECENT
29:00 Flux Pavilion - Bass Cannon (Coffi Remix) CIRCUS RECORDS
29:30 Samplifire - Mercia DISCIPLE
30:48 NGHTMRE - Street (PEEKABOO Remix) MAD DECENT
32:00 UBUR & Aweminus & YAKZ - Party Starter SELF RELEASED
33:20 Flosstradamus & Valentino Khan - MFU ULTRA/FOOL'S GOLD
33:22 w/ MARAUDA - Umbra MALIGNANT
34:30 Young Money ft. Drake - Trophies CASH MONEY
36:01 w/ Megalodon & Antiserum - Platinum NEVER SAY DIE
36:20 GRiZ & JAUZ - No Doubt DEADBEATS
38:20 Spag Heddy - Spaghetti Slap TOMATO BASS
38:57 Alice Deejay - Better Off Alone VIOLENT
40:09 w/ Yeah Yeah Yeahs & A-Trak & Kid Kamillion vs. Rihanna vs. Mightyfools & Yellow Claw & Hasse De Moor - Heads Will Roll vs. Work vs. Lick Dat (Flosstradamus Edit)
DGC / BARONG FAMILY / ROC NATION
41:40 JAUZ & DJ Snake - Gassed Up (Izadi Flip) BITE THIS!
42:00 Kompany & Wooli - Fight Milk OPHELIA
42:35 Marshmello & SVDDEN DEATH - Crusade (VIP) JOYTIME COLLECTIVE
43:10 Subtronics - Cabin Fever CYCLOPS
43:45 Zombie Nation - Kernkraft 400 (W&W Remix) FREE/GIGOLO
   w/ NGHTMRE & Subtronics ft. Boogie T - Nuclear Bass Face ULTRA
45:00 RL Grime & Juelz vs. Lil Nas X & Jack Harlow vs. Deadlyft - Formula vs. Industry Baby vs. SMD (CELO & Noname Edit)
46:20 JAUZ & FIRST - Velvet Paradise (Franky Nuts & Oliverse Remix) BITE THIS!
46:22 w/ Deadlyft - SMD SELF RELEASED
48:10 Post Malone - Hollywood's Bleeding (JAUZ Remix) REPUBLIC (UMG)
50:00 JAUZ & Masked Wolf - Mercy SPINNIN'
50:33 GTA ft. DJ Funk - Booty Bounce (GTA HYPRR MIX) FREE/MAD DECENT
51:07 w/ Skrillex & Rick Ross - Purple Lamborghini ATLANTIC (WARNER MUSIC)
51:12 w/ PhaseOne ft. Shane Told Of Silverstein - Enemy (VIP) DISCIPLE
   w/ Eurythmics - Sweet Dreams (Acappella) RCA (SONY)
52:00 NGHTMRE & Deadlyft - Ring The Alarm GUD VIBRATIONS
53:30 Ace Aura - Gem World NEVER SAY DIE
54:00 Trippie Redd ft. Playboi Carti - Miss The Rage (Crankdat Remix) TENTHOUSAND PROJECTS
55:20 Don Toliver & Knock2 vs. BROKN - Cardigan vs. Fallout (TELLAH & SLICK Edit)
56:30 GTA - Saria's Turn Up (JAUZ & Barely Alive Remix) FREE
   w/ GTA & Valentino Khan - Break Your Neck (Acappella) THREE SIX ZERO
   w/ GRiZ ft. Subtronics - Griztronics DEADBEATS
   w/ Beyoncé - 7/11 (Jack Ü Remix) FREE/COLUMBIA
58:05 SLANDER & WAVEDASH - Move Back INSOMNIAC
58:35 The Chainsmokers - High(Co-Prod. by Whethan) (Crankdat Remix) DISRUPTOR (SONY)
 The Kid LAROI - Without You (JAUZ Remix) (Instrumental) COLUMBIA (SONY)
1:00:10 PEEKABOO & Eptic - NOSEBLEED PEEKABOO
1:00:10 w/ BOOG - DEADLY HORSE RITUAL SELF RELEASED
1:01:15 Benny Benassi ft. Gary Go vs. Snavs - Cinema vs. Lust (Snavs Edit)
ULTRA / RIOTVILLE
   w/ Leotrix - FUNNYFACE MONSTERCAT
1:02:40 Eliminate & PEEKABOO - Quickness BASSRUSH
1:03:35 Pharoahe Monch - Simon Says TRESCADECAPHOBIA
1:04:40 w/ JAUZ & Zeds Dead - Shake DEADBEATS/BITE THIS!
1:05:20 Corona - The Rhythm Of The Night ZYX
1:05:39 w/ Skrillex - Scary Monsters And Nice Sprites BIG BEAT/MAU5TRAP
1:06:12 w/ AFK & Carbin ft. Cody Ray - Boss BITE THIS!
1:06:23 w/ HEYZ ft. Maylyn - Castaway King (AFK Remix) BITE THIS!
1:06:50 Kanye West - Power ROC-A-FELLA (ISLAND DEF JAM)
   w/ Knife Party - PLUR Police (JAUZ Remix) EARSTORM
1:08:50 Evalution - Roll It Up BITE THIS!
1:09:20 NGHTMRE - Street (VIP) MAD DECENT
   w/ LYNY - Kill Count SELF RELEASED
1:10:25 G Jones - In Your Head (RL Grime Edit) SABLE VALLEY
1:10:47 w/ Barely Alive & Control Freak - Tick Tock DISCIPLE
1:11:20 MARAUDA - Swathe MALIGNANT
1:12:00 PhaseOne - Into The Light DISCIPLE
1:13:10 SVDDEN DEATH - DREAM SEQUENCE VOYD
1:15:15 JAUZ & Zeds Dead - Lights Go Down (ID Remix) DEADBEATS/BITE THIS!
   w/ Enei - Sinking CRITICAL
1:17:38 Travis Scott ft. Drake - Sicko Mode (UPGRADE Jump Up Booty) EPIC (SONY BMG)
1:18:45 Mark Knight ft. Skin - Nothing Matters (Noisia Remix) TOOLROOM
1:20:00 Eptic - Payback MONSTERCAT
1:21:00 JAUZ & Dimension - ID
1:22:00 NGHTMRE & WAVEDASH - Grave MAD DECENT
1:23:10 SLANDER & NGHTMRE ft. Matthew Santos - Feeling Gud GUD VIBRATIONS
1:26:18 SHAED - Trampoline (JAUZ Remix) PHOTO FINISH
"""
```
## Contributing

Everyone is welcome to contribute!

