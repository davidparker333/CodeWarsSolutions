# YouTube had a like and a dislike button, which allowed users to express their opinions about particular content.
#  It was set up in such a way that you cannot like and dislike a video at the same time. There are two other
# interesting rules to be noted about the interface: Pressing a button, which is already active, will undo your press.
# If you press the like button after pressing the dislike button, the like button overwrites the previous "Dislike" state.
# The same is true for the other way round.

# Task
# Create a function that takes in a list of button inputs and returns the final state.

# Examples
# like_or_dislike([Dislike]) ➞ Dislike
# like_or_dislike([Like, Like]) ➞ Nothing
# like_or_dislike([Dislike, Like]) ➞ Like
# like_or_dislike([Like, Dislike, Dislike]) ➞ Nothing
# Notes
# If no button is currently active, return Nothing.
# If the list is empty, return Nothing.

# Like, Dislike, Nothing come from Preloaded
def like_or_dislike(lst):
    val = 'Nothing'
    for x in lst:
        if x == 'Like':
            if val == 'Like':
                val = 'Nothing'
                continue
            val = 'Like'
        elif x == 'Dislike':
            if val == 'Dislike':
                val = 'Nothing'
                continue
            val = 'Dislike'
    return val


print(like_or_dislike(['Dislike']))
