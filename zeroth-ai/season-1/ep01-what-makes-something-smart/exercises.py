"""
Zeroth: AI — Episode 1 Exercises
What Makes Something Smart?

The big idea: AI is a machine that figures out rules from experience,
instead of being told the rules by a programmer.

These exercises let you see the difference firsthand.
"""

# ─── Exercise 1: The Thermostat (Rule-Based) ────────────────────────────
#
# This is NOT AI. A human wrote the rule. The thermostat follows it blindly.


def thermostat(temperature, target=68):
    """A thermostat follows a fixed rule. No learning. No adaptation."""
    if temperature < target:
        return "HEAT ON"
    else:
        return "HEAT OFF"


print("=== Exercise 1: The Thermostat ===")
print(f"Temperature 65°F → {thermostat(65)}")
print(f"Temperature 70°F → {thermostat(70)}")
print(f"Temperature 68°F → {thermostat(68)}")
print()
print("The thermostat doesn't know what temperature IS.")
print("It doesn't know what heat IS. It just follows the rule.")
print()


# ─── Exercise 2: Rule-Based Spam Filter (The Old Way) ───────────────────
#
# Early spam filters used word lists. Programmers wrote the rules by hand.
# Spammers changed the words. Arms race.

SPAM_WORDS = ["free", "winner", "click here", "act now", "limited time"]


def rule_based_spam(email_text):
    """Check if any banned word appears. Programmer wrote these rules."""
    text_lower = email_text.lower()
    for word in SPAM_WORDS:
        if word in text_lower:
            return "SPAM"
    return "NOT SPAM"


print("=== Exercise 2: Rule-Based Spam Filter ===")
emails = [
    "Congratulations! You're a WINNER! Click here to claim!",
    "Hey, are you free for lunch tomorrow?",
    "LIMITED TIME offer! Act now!",
    "Meeting moved to 3pm, conference room B",
    "You've won a FR33 iPhone! W1NNER!",  # spammer evading the rules
]
for email in emails:
    result = rule_based_spam(email)
    print(f"  {result:>8} | {email[:60]}")

print()
print("Notice: 'FR33' and 'W1NNER' bypass the filter.")
print("The spammer changed spelling. The rule-based filter can't adapt.")
print()


# ─── Exercise 3: Learning Spam Filter (The AI Way) ──────────────────────
#
# Instead of rules, we LEARN patterns from examples.
# This is the simplest possible "machine learning" — counting word frequencies.


def train_spam_detector(training_data):
    """Learn which words appear more in spam vs. not-spam."""
    spam_words = {}
    ham_words = {}

    for text, label in training_data:
        words = text.lower().split()
        bucket = spam_words if label == "spam" else ham_words
        for word in words:
            bucket[word] = bucket.get(word, 0) + 1

    return spam_words, ham_words


def predict_spam(text, spam_words, ham_words):
    """Score an email based on learned word frequencies."""
    words = text.lower().split()
    spam_score = 0
    ham_score = 0

    for word in words:
        spam_score += spam_words.get(word, 0)
        ham_score += ham_words.get(word, 0)

    return "SPAM" if spam_score > ham_score else "NOT SPAM"


training_data = [
    ("free money click here winner prize", "spam"),
    ("act now limited time offer deal", "spam"),
    ("congratulations you won amazing prize", "spam"),
    ("claim your free gift card today", "spam"),
    ("meeting at 3pm conference room", "not spam"),
    ("can you review the quarterly report", "not spam"),
    ("lunch tomorrow at noon?", "not spam"),
    ("project deadline moved to friday", "not spam"),
    ("great job on the presentation today", "not spam"),
]

spam_words, ham_words = train_spam_detector(training_data)

print("=== Exercise 3: Learning Spam Filter ===")
test_emails = [
    "You won a free prize! Claim now!",
    "Can we move the meeting to 2pm?",
    "Amazing deal on a gift card today",
    "Quarterly report is ready for review",
]
for email in test_emails:
    result = predict_spam(email, spam_words, ham_words)
    print(f"  {result:>8} | {email}")

print()
print("Nobody programmed a word list. The system learned from examples.")
print("That's the difference. That's what makes it AI.")
print()


# ─── Exercise 4: The Intelligence Spectrum ──────────────────────────────

print("=== Exercise 4: The Intelligence Spectrum ===")
print()
spectrum = [
    ("Thermostat", "Follows 1 rule", "Zero learning"),
    ("Calculator", "Follows complex rules", "Zero understanding"),
    ("Spam filter (rules)", "Follows word list", "Programmer adapts it"),
    ("Spam filter (ML)", "Learns from examples", "Adapts on its own"),
    ("Your dog", "Learns from experience", "Generalizes to new situations"),
    ("Chess computer", "Evaluates positions", "Can't recognize a cat"),
    (
        "Three-year-old",
        "Bad at chess",
        "Recognizes faces, learns language, catches balls",
    ),
]

print(f"{'System':<22} {'What it does':<28} {'Key limitation/ability'}")
print("-" * 80)
for name, does, limit in spectrum:
    print(f"{name:<22} {does:<28} {limit}")
print()
print("Intelligence isn't one thing. It's many things.")
print("Moravec's Paradox: what's easy for humans is hard for machines, and vice versa.")
