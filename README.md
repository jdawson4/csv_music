# csv_music
This branch of csv_music is designed to create music independently of the length of the notes being played.


Converts CSV files (made by a .midi to .csv converter) into a file that only contains notes (and back again).

Inspired by this video by YouTuber Carykh: https://www.youtube.com/watch?v=SacogDL_4JU
This repository contains files used to turn .csv files into .cust files (just a name I made) and back again for use in Andrej Karpathy's character-based RNN (found here:https://github.com/karpathy/char-rnn).

I converted the .midi files into .csv files using this utilty: http://www.fourmilab.ch/webtools/midicsv/.

This branch differs from the master in that it *should* be able to learn how to make rhythms-- the RNN should be able to see the length of the notes in the training file and reproduce them in the sample file. This is done through the csv_music converter by writing lots of notes where the notes are long and then being able to count the length of notes inputted into it.
