
"""
🔐 ASCII Code Word Program
"""

PASSWORD = "1234"  # You can change this password

print("✨ Welcome to the ASCII Code Word Converter! ✨")

# Step 1: Take text input
text = input("\n✏️ Enter the text to convert into ASCII: ")

# Convert text to ASCII
ascii_values = [ord(ch) for ch in text]
print(f"🔢 ASCII Conversion: {ascii_values}")

# Step 2: Ask if user wants to decode
choice = input("\n❓ Do you want to decode the ASCII back to text? (yes/no): ").strip().lower()

if choice == "yes":
    # Ask for password
    entered_pass = input("🔑 Enter the password: ")

    if entered_pass == PASSWORD:
        decoded_text = ''.join(chr(num) for num in ascii_values)
        print(f"✅ Decoded Text: {decoded_text}")
    else:
        print("❌ Access Denied! Wrong Password.")
else:
    print("👍 Okay! Conversion completed.")
