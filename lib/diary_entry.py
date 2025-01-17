class DiaryEntry:
    def __init__(self, title, contents):
        self._title = title
        self._contents = contents

    def format(self):
        return f"{self._title}{self._contents}"
        

    def count_words(self):
        return len(self._contents)

    def reading_time(self, wpm):
        reading_count = len(self._contents.split())
        
        return round(reading_count / wpm)
        

    def reading_chunk(self, wpm, minutes):
        
        words_user_can_read = wpm * minutes
        words = self._contents.split()
        chunk = words[:words_user_can_read]
        return " ".join(chunk)



        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.