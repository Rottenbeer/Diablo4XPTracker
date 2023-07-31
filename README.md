# Diablo IV Nightmare Dungeon Experience Tracker

Track your gained experience in nightmare dungeons with two simple screenshots of the xp bar at the start and the end of the dungeon (check the example below).
Use the hotkey defined in the Diablo IV hotkey menu and set the path to the screenshot folder accordingly (See section "Configuration").
![Example Screenshot](screenshot.jpg)

ORC done via [Tesseract OCR](https://github.com/tesseract-ocr/tesseract), which needs to be installed.

## Configuration
Diablo4XPTracker requires a config file that contains a path to the Diablo IV screenshot directory, the Tesseract executable and the
coordinates of a box round your dungeon name and xp box next to the executable. The defaults are fitting for 1440p. Please look at the following screenshot to determine
the coordinates you need in case you don't have a 1440p monitor. The 4 numbers represent the left(x), top(y), right(x) and bottom(y) values of the
bounding box.
![Coordinates Demo](coordinate_image.jpg)

## Example output:
    python.exe .\main.py
    2023-07-29 19:21:28,604 - xp_tracker.py - root - INFO - Diablo IV Nightmare Dungeon Experience Tracker
    2023-07-29 19:21:44,616 - dungeonmanager.py - root - INFO - Gained 1,012,878 XP in Hoarfrost Demise. It took 0:05:14.188513 XP/H: 11,605,646.45!
    2023-07-29 19:21:44,616 - dungeonmanager.py - root - INFO - Gained 1,171,716 XP in Mercy's Reach. It took 0:04:58.720414 XP/H: 14,120,821.35!
    2023-07-29 19:21:44,616 - dungeonmanager.py - root - INFO - Gained 1,211,186 XP in Mercy's Reach. It took 0:08:14.664258 XP/H: 8,814,604.11!
    2023-07-29 19:21:44,616 - dungeonmanager.py - root - INFO - Gained 1,195,237 XP in Mercy's Reach. It took 0:04:24.340302 XP/H: 16,277,704.03!
    2023-07-29 19:21:44,616 - dungeonmanager.py - root - INFO - Gained 1,028,738 XP in Mercy's Reach. It took 0:05:24.722217 XP/H: 11,404,999.74!
    2023-07-29 19:21:44,616 - dungeonmanager.py - root - INFO - Gained 1,377,757 XP in Uldur's Cave. It took 0:05:16.865495 XP/H: 15,653,093.44!
    2023-07-29 19:21:44,616 - dungeonmanager.py - root - INFO - Gained 986,494 XP in Komdor Temple. It took 0:04:43.125941 XP/H: 12,543,458.18!
    2023-07-29 19:21:44,616 - dungeonmanager.py - root - INFO - Gained 1,460,081 XP in Komdor Temple. It took 0:08:25.829407 XP/H: 10,391,431.43!
    2023-07-29 19:21:44,616 - dungeonmanager.py - root - INFO - Gained 1,125,642 XP in Sarat's Lair. It took 0:03:57.504993 XP/H: 17,062,004.25!
    2023-07-29 19:21:44,616 - dungeonmanager.py - root - INFO - Gained 954,492 XP in Sarat's Lair. It took 0:02:52.022515 XP/H: 19,975,124.77!
    2023-07-29 19:21:44,616 - dungeonmanager.py - root - INFO - Gained 1,143,142 XP in Sarat's Lair. It took 0:02:50.285557 XP/H: 24,167,118.30!
    2023-07-29 19:21:44,617 - dungeonmanager.py - root - INFO - Gained 1,186,014 XP in Sarat's Lair. It took 0:02:49.635464 XP/H: 25,169,562.42!

## Exported CSV:
    Mercy's Reach,97,3379459,2023-07-29 17:39:38.981402,97,4551175,2023-07-29 17:44:37.701816,1171716,0:04:58.720414,14120821.351030935
    Mercy's Reach,97,4556243,2023-07-29 17:46:54.660248,97,5767429,2023-07-29 17:55:09.324506,1211186,0:08:14.664258,8814604.106690885
    Mercy's Reach,97,5767429,2023-07-29 17:55:17.793420,97,6962666,2023-07-29 17:59:42.133722,1195237,0:04:24.340302,16277704.033189762
    Mercy's Reach,97,6962666,2023-07-29 18:01:52.501719,97,7991404,2023-07-29 18:07:17.223936,1028738,0:05:24.722217,11404999.738591956
    Uldur's Cave,97,7991404,2023-07-29 18:12:40.866426,97,9369161,2023-07-29 18:17:57.731921,1377757,0:05:16.865495,15653093.436380632
    Komdor Temple,97,9377503,2023-07-29 18:20:49.268701,97,10363997,2023-07-29 18:25:32.394642,986494,0:04:43.125941,12543458.177857323
    Komdor Temple,97,10363997,2023-07-29 18:29:06.913752,97,11824078,2023-07-29 18:37:32.743159,1460081,0:08:25.829407,10391431.4337205
    Sarat's Lair,97,11824078,2023-07-29 18:39:01.357910,97,12949720,2023-07-29 18:42:58.862903,1125642,0:03:57.504993,17062004.25015907
    Sarat's Lair,97,13136522,2023-07-29 18:43:52.474405,97,14091014,2023-07-29 18:46:44.496920,954492,0:02:52.022515,19975124.767824724
    Sarat's Lair,97,14274676,2023-07-29 18:48:53.857189,97,15417818,2023-07-29 18:51:44.142746,1143142,0:02:50.285557,24167118.295299698
    Sarat's Lair,97,15599818,2023-07-29 18:53:31.706395,97,16785832,2023-07-29 18:56:21.341859,1186014,0:02:49.635464,25169562.421216354