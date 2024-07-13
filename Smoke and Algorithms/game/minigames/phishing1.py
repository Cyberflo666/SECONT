import pygame
import sys
import random
import time

def phishing_game():
    # Initialize Pygame
    pygame.init()

    # Screen settings for smartphone aspect ratio
    SCREEN_WIDTH, SCREEN_HEIGHT = 1024, 1024  # Larger screen size
    GAME_WIDTH, GAME_HEIGHT = 400, 600  # Define the size of the gaming area
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Email Viewer")

    # Load background image
    background_image = pygame.image.load("smartphone.png")  # Background image named smartphone.png
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    DARK_BLUE = (0, 0, 150)
    DARK_RED = (150, 0, 0)
    GREY = (200, 200, 200)
    DARK_GREY = (169, 169, 169)

    # Fonts
    header_font = pygame.font.Font(None, 25)  # Larger font size
    email_font = pygame.font.Font(None, 18)  # Larger font size
    button_font = pygame.font.Font(None, 27)  # Larger font size

    # Define a list of emails with different properties
    emails = [
        {
            "sender": "Support Team <support@yourbank.com>",
            "recipient": "YourEmail@example.com",
            "subject": "Urgent: Unauthorized Access Detected",
            "date": "Mon, 10 Jun 2024 09:30:00 -0700",
            "text": (
                "Dear Valued Customer,\n\n"
                "We detected unauthorized access attempts on your bank account. "
                "For your security, please verify your identity by clicking the link below:\n\n"
                "https://www.yourbank.com/security-alert\n\n"
                "Thank you for your prompt attention.\n\n"
                "Support Team"
            ),
            "legitimate": False
        },
        {
            "sender": "Friendship Club <noreply@friendshipclub.com>",
            "recipient": "YourEmail@example.com",
            "subject": "Exclusive Offer Inside! 🎁",
            "date": "Tue, 11 Jun 2024 12:45:00 -0700",
            "text": (
                "Hello Friend,\n\n"
                "As a valued member of our Friendship Club, we have an exclusive offer just for you! "
                "Click the link below to claim your free gift:\n\n"
                "https://www.friendshipclub.com/free-gift\n\n"
                "We appreciate your friendship!\n\n"
                "Friendship Club Team"
            ),
            "legitimate": False
        },
        {
            "sender": "Nigerian Prince <prince@kingdomofnigeria.com>",
            "recipient": "YourEmail@example.com",
            "subject": "Urgent Business Proposal 🌟",
            "date": "Wed, 12 Jun 2024 15:00:00 -0700",
            "text": (
                "Dear Esteemed One,\n\n"
                "I am a Nigerian Prince seeking your assistance in a matter of great importance. "
                "If you can help, you will be generously rewarded. Please reply to this email to learn more.\n\n"
                "Sincerely,\n"
                "Prince [Name]"
            ),
            "legitimate": False
        },
        {
            "sender": "Health Insurance <info@medicalinsurance.com>",
            "recipient": "YourEmail@example.com",
            "subject": "Important Health Plan Update",
            "date": "Thu, 13 Jun 2024 08:30:00 -0700",
            "text": (
                "Dear Policyholder,\n\n"
                "We have made updates to your health insurance plan. "
                "Please review the changes and confirm your understanding by clicking the link below:\n\n"
                "https://www.medicalinsurance.com/plan-update\n\n"
                "Thank you for choosing us for your healthcare needs.\n\n"
                "Health Insurance Team"
            ),
            "legitimate": True
        },
        {
            "sender": "Tax Agency <no-reply@taxauthority.gov>",
            "recipient": "YourEmail@example.com",
            "subject": "Tax Refund Notification",
            "date": "Fri, 14 Jun 2024 10:20:00 -0700",
            "text": (
                "Dear Taxpayer,\n\n"
                "We are pleased to inform you that you are eligible for a tax refund. "
                "To claim your refund, please fill out the form provided at the following link:\n\n"
                "https://www.taxauthority.gov/refund-claim\n\n"
                "Thank you for your cooperation.\n\n"
                "Tax Agency"
            ),
            "legitimate": False
        },
        {
            "sender": "Survey Company <survey@opinionpolls.com>",
            "recipient": "YourEmail@example.com",
            "subject": "Your Opinion Matters!",
            "date": "Sat, 15 Jun 2024 11:45:00 -0700",
            "text": (
                "Hello,\n\n"
                "We invite you to participate in a brief survey. Your feedback is valuable to us "
                "and will help improve our services. Click the link below to get started:\n\n"
                "https://www.opinionpolls.com/survey\n\n"
                "Thank you for your time.\n\n"
                "Survey Company"
            ),
            "legitimate": True
        },
        {
            "sender": "Job Opportunity <careers@dreamjob.com>",
            "recipient": "YourEmail@example.com",
            "subject": "Exciting Job Opportunity Awaits!",
            "date": "Sun, 16 Jun 2024 14:30:00 -0700",
            "text": (
                "Dear Job Seeker,\n\n"
                "We have an exciting job opportunity that matches your skills and experience. "
                "Click the link below to learn more and apply:\n\n"
                "https://www.dreamjob.com/job-opportunity\n\n"
                "Don't miss out on this chance!\n\n"
                "Dream Job Team"
            ),
            "legitimate": True
        },
        {
            "sender": "Secret Admirer <anonymous@secretlove.com>",
            "recipient": "YourEmail@example.com",
            "subject": "A Special Message Just for You ❤️",
            "date": "Mon, 17 Jun 2024 16:00:00 -0700",
            "text": (
                "Dear Beloved,\n\n"
                "I have admired you from afar and wish to express my feelings. "
                "Please open the attached file to read my heartfelt message.\n\n"
                "With love,\n"
                "Your Secret Admirer"
            ),
            "legitimate": False
        },
        {
            "sender": "Free Prize <prizes@freegiveaway.com>",
            "recipient": "YourEmail@example.com",
            "subject": "Congratulations! You've Won!",
            "date": "Tue, 18 Jun 2024 09:00:00 -0700",
            "text": (
                "Congratulations!\n\n"
                "You are the lucky winner of our grand prize giveaway. "
                "To claim your prize, simply provide your personal information by clicking the link below:\n\n"
                "https://www.freegiveaway.com/claim-prize\n\n"
                "Best regards,\n"
                "Free Giveaway Team"
            ),
            "legitimate": False
        },
        {
            "sender": "Tech Support <support@techhelp.com>",
            "recipient": "YourEmail@example.com",
            "subject": "Important System Update",
            "date": "Wed, 19 Jun 2024 12:30:00 -0700",
            "text": (
                "Dear User,\n\n"
                "We have released an important system update to enhance security and performance. "
                "Please install the update by clicking the link below:\n\n"
                "https://www.techhelp.com/system-update\n\n"
                "Thank you for your cooperation.\n\n"
                "Tech Support Team"
            ),
            "legitimate": True
        },
        {
            "sender": "Amazon <no-reply@amazon.com>",
            "recipient": "YourEmail@example.com",
            "subject": "Your recent order #12345",
            "date": "Fri, 14 May 2024 12:34:56 -0700",
            "text": (
                "Hello,\n\n"
                "Your order has been successfully processed and will be delivered soon.\n\n"
                "Thank you for shopping with us!\n\n"
                "Amazon Team"
            ),
            "legitimate": True
        },
        {
            "sender": "Newsletter <newsletter@info.com>",
            "recipient": "YourEmail@example.com",
            "subject": "Weekly News Update",
            "date": "Fri, 14 Jun 2024 08:00:00 -0700",
            "text": (
                "Hello,\n\n"
                "Here is your weekly news update. Stay informed with the latest headlines.\n\n"
                "Best regards,\n"
                "News Team"
            ),
            "legitimate": True
        },
    ]

    # Define button dimensions and positions
    BUTTON_WIDTH = 120
    BUTTON_HEIGHT = 50
    BUTTON_X = (SCREEN_WIDTH - BUTTON_WIDTH) // 2
    LEGIT_BUTTON_Y = SCREEN_HEIGHT - 200
    PHISH_BUTTON_Y = SCREEN_HEIGHT - 120

    # Game variables
    score = 0
    email_index = 0

    # Function to draw a button
    def draw_button(text, x, y, color, hover_color):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + BUTTON_WIDTH > mouse[0] > x and y + BUTTON_HEIGHT > mouse[1] > y:
            pygame.draw.rect(screen, hover_color, (x, y, BUTTON_WIDTH, BUTTON_HEIGHT))
            if click[0] == 1:
                return True
        else:
            pygame.draw.rect(screen, color, (x, y, BUTTON_WIDTH, BUTTON_HEIGHT))

        button_text = button_font.render(text, True, WHITE)
        screen.blit(button_text, (x + (BUTTON_WIDTH - button_text.get_width()) // 2,
                                  y + (BUTTON_HEIGHT - button_text.get_height()) // 2))
        return False

    # Game loop
    running = True
    while running:
        screen.fill(WHITE)
        screen.blit(background_image, (0, 0))

        # Draw the current email
        if email_index < len(emails):
            email = emails[email_index]

            # Display email details within the smartphone screen area
            margin = 50
            display_width = GAME_WIDTH - 2 * margin
            display_height = GAME_HEIGHT - 2 * margin

            header_y = margin
            sender_text = header_font.render("Sender: " + email["sender"], True, BLACK)
            screen.blit(sender_text, (margin, header_y))

            recipient_text = header_font.render("To: " + email["recipient"], True, BLACK)
            screen.blit(recipient_text, (margin, header_y + 30))

            subject_text = header_font.render("Subject: " + email["subject"], True, BLACK)
            screen.blit(subject_text, (margin, header_y + 60))

            date_text = header_font.render("Date: " + email["date"], True, BLACK)
            screen.blit(date_text, (margin, header_y + 90))

            text_lines = email["text"].split('\n')
            for i, line in enumerate(text_lines):
                email_line_text = email_font.render(line, True, BLACK)
                screen.blit(email_line_text, (margin, header_y + 130 + i * 25))

            # Draw buttons
            if draw_button("Legitimate", BUTTON_X, LEGIT_BUTTON_Y, DARK_BLUE, BLUE):
                if email["legitimate"]:
                    score += 1
                email_index += 1
                time.sleep(0.2)  # Add a short delay for button press feedback
            if draw_button("Phishing", BUTTON_X, PHISH_BUTTON_Y, DARK_RED, RED):
                if not email["legitimate"]:
                    score += 1
                email_index += 1
                time.sleep(0.2)  # Add a short delay for button press feedback
        else:
            # Game over screen
            game_over_text = header_font.render("Game Over! Your score: " + str(score), True, BLACK)
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2))

            if draw_button("Exit", BUTTON_X, PHISH_BUTTON_Y, DARK_GREY, GREY):
                running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    pygame.quit()
    return score

if __name__ == "__main__":
    print(phishing_game())
