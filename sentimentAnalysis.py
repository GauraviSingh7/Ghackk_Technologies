from textblob import TextBlob

# Expanded comments dataset
comments = [
    "I love manga and manhwa! They are both amazing!",
    "Manga has a unique art style that I really appreciate.",
    "Manhwa is way better than manga in terms of story.",
    "I don't like the pacing of some manga.",
    "The characters in manhwa are often more relatable.",
    "I prefer manga because it's usually more detailed.",
    "Manhwa just doesn't hit the same for me.",
    "Both are good in their own ways, but I lean towards manhwa.",
    "Manga can be a bit repetitive at times.",
    "I find the art in manhwa to be more appealing.",
    "The storylines in manga are often more engaging than manhwa.",
    "I enjoy the longer episodes in manhwa.",
    "Manga feels more nostalgic for me.",
    "Some manhwa have beautiful illustrations!",
    "Manga has better character development.",
    "I love how manhwa often features color pages.",
    "Manga can sometimes have confusing plots.",
    "Manhwa has introduced me to so many new genres.",
    "The pacing in manhwa feels smoother overall.",
    "I appreciate the cultural differences presented in both.",
    "Manga is a classic and always holds a special place in my heart.",
    "I find manga to be more immersive than manhwa.",
    "The humor in manhwa is often more relatable.",
    "I enjoy the unique storytelling style in manhwa.",
    "Manga often feels more mature and sophisticated.",
    "Manhwa has more diverse genres available.",
    "I dislike when manga gets too long and drawn out.",
    "The emotional depth in manhwa is sometimes lacking.",
    "I love the way manga often explores complex themes.",
    "Manhwa can be a bit too focused on romance for my taste.",
    "I enjoy the character designs in both manga and manhwa.",
    "Manga tends to have more action-packed stories.",
    "Some manhwa feel like they're just copies of popular manga.",
    "I appreciate how manhwa often features strong female leads.",
    "Manga sometimes leaves me wanting more at the end.",
    "Manhwa's art style is often vibrant and colorful.",
    "I think manga has better pacing in storytelling.",
    "Manhwa can feel more accessible to new readers.",
    "I enjoy the world-building in both formats.",
    "Manga often explores darker themes than manhwa.",
    "I love how manhwa can blend different genres seamlessly.",
    "Manga usually has a more traditional art style.",
    "Some of my favorite stories come from manhwa.",
    "I think both have their strengths and weaknesses.",
    "The fandom for manga feels more dedicated overall.",
    "Manhwa sometimes lacks the depth of character arcs found in manga."
]

# Initialize counters for sentiment
positive_count = 0
negative_count = 0

# Analyze sentiment of each comment
for comment in comments:
    analysis = TextBlob(comment)
    # Classify as positive or negative based on polarity
    if analysis.sentiment.polarity > 0:
        positive_count += 1
    elif analysis.sentiment.polarity < 0:
        negative_count += 1

# Calculate percentages
total_comments = len(comments)
positive_percentage = (positive_count / total_comments) * 100
negative_percentage = (negative_count / total_comments) * 100

# Print results
print(f"Total Comments: {total_comments}")
print(f"Positive Comments: {positive_count} ({positive_percentage:.2f}%)")
print(f"Negative Comments: {negative_count} ({negative_percentage:.2f}%)")
