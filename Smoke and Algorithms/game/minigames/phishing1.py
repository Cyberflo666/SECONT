import pygame
import sys
import random
import time
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
            "Your order has been successfully processed and will be delivered soon. "
            "Thank you for shopping with us!\n\n"
            "Order Summary:\n"
            "- Item: Book 'Learning Python'\n"
            "- Quantity: 1\n"
            "- Price: $29.99\n\n"
            "If you have any questions, please contact our support team.\n\n"
            "Best regards,\n"
            "Amazon Customer Service\n\n"
            "Call to Action: Click the link below to track your order.\n"
            "https://www.amazon.com/trackorder"
        ),
        "legitimate": True
    },
    {
        "sender": "Apple <no-reply@apple.com>",
        "recipient": "YourEmail@example.com",
        "subject": "Your Apple ID has been compromised!",
        "date": "Mon, 17 May 2024 09:45:32 -0700",
        "text": (
            "Dear Customer,\n\n"
            "We regret to inform you that your Apple ID has been compromised. "
            "Please click the link below to verify your account and secure your information.\n\n"
            "https://fakephishingsite.com\n\n"
            "Failure to take action may result in permanent suspension of your account.\n\n"
            "Sincerely,\n"
            "Apple Support"
        ),
        "legitimate": False
    },
    {
        "sender": "Netflix <no-reply@netflix.com>",
        "recipient": "YourEmail@example.com",
        "subject": "Your account has been suspended!",
        "date": "Tue, 18 May 2024 15:20:17 -0700",
        "text": (
            "Dear User,\n\n"
            "We regret to inform you that your Netflix account has been suspended due to "
            "suspicious activity. Please click the link below to verify your identity and reactivate your account.\n\n"
            "https://fakephishingsite.com\n\n"
            "Failure to take action may result in permanent suspension of your account.\n\n"
            "Best regards,\n"
            "Netflix Support"
        ),
        "legitimate": False
    },
    {
        "sender": "Google <no-reply@google.com>",
        "recipient": "YourEmail@example.com",
        "subject": "Important security update for your Google account",
        "date": "Wed, 19 May 2024 10:15:00 -0700",
        "text": (
            "Dear User,\n\n"
            "We've noticed some unusual activity on your Google account. "
            "To ensure the security of your account, please review your recent activity and take appropriate actions.\n\n"
            "If you suspect any unauthorized access, please visit the following link to secure your account:\n\n"
            "https://accounts.google.com/SecurityCheckup\n\n"
            "Best regards,\n"
            "Google Security Team"
        ),
        "legitimate": True
    },
    {
        "sender": "PayPal <no-reply@paypal.com>",
        "recipient": "YourEmail@example.com",
        "subject": "Your account has been temporarily limited!",
        "date": "Thu, 20 May 2024 14:30:45 -0700",
        "text": (
            "Dear Customer,\n\n"
            "We regret to inform you that your PayPal account has been temporarily limited due to "
            "security reasons. Please click the link below to verify your identity and restore full access to your account.\n\n"
            "https://fakephishingsite.com\n\n"
            "Failure to take action may result in permanent suspension of your account.\n\n"
            "Sincerely,\n"
            "PayPal Security Team"
        ),
        "legitimate": False
    },
    {
        "sender": "Microsoft <no-reply@microsoft.com>",
        "recipient": "YourEmail@example.com",
        "subject": "Account Security Alert",
        "date": "Mon, 03 Jun 2024 10:15:22 -0700",
        "text": (
            "Dear User,\n\n"
            "We have detected unusual activity on your Microsoft account. "
            "To ensure the security of your account, please verify your identity by clicking the link below:\n\n"
            "https://account.microsoft.com/security\n\n"
            "Thank you for your cooperation.\n\n"
            "Microsoft Support"
        ),
        "legitimate": False
    },
    {
        "sender": "Amazon <no-reply@amazon.com>",
        "recipient": "YourEmail@example.com",
        "subject": "Your Recent Purchase",
        "date": "Tue, 04 Jun 2024 09:30:45 -0700",
        "text": (
            "Hello,\n\n"
            "Thank you for your recent purchase. "
            "Your order has been successfully processed and will be delivered shortly. "
            "If you have any questions regarding your order, please feel free to contact us.\n\n"
            "Best regards,\n"
            "Amazon Customer Service"
        ),
        "legitimate": True
    },
    {
        "sender": "PayPal <service@paypal.com>",
        "recipient": "YourEmail@example.com",
        "subject": "Account Security Notification",
        "date": "Wed, 05 Jun 2024 13:45:18 -0700",
        "text": (
            "Dear Customer,\n\n"
            "We have detected a login attempt from an unrecognized device on your PayPal account. "
            "To secure your account, please verify your identity by clicking the link below:\n\n"
            "https://www.paypal.com/signin/verify\n\n"
            "Thank you for choosing PayPal.\n\n"
            "PayPal Security Team"
        ),
        "legitimate": False
    },
    {
        "sender": "Apple Support <noreply@apple.com>",
        "recipient": "YourEmail@example.com",
        "subject": "Your Apple ID has been locked",
        "date": "Thu, 06 Jun 2024 16:20:30 -0700",
        "text": (
            "Dear Apple Customer,\n\n"
            "We regret to inform you that your Apple ID has been locked due to suspicious activity. "
            "To regain access to your account, please update your security information by clicking the link below:\n\n"
            "https://appleid.apple.com/account/manage\n\n"
            "Thank you for your cooperation.\n\n"
            "Apple Support"
        ),
        "legitimate": False
    },
    {
        "sender": "Netflix <support@netflix.com>",
        "recipient": "YourEmail@example.com",
        "subject": "Account Verification Required",
        "date": "Fri, 07 Jun 2024 11:55:10 -0700",
        "text": (
            "Dear Netflix User,\n\n"
            "We are unable to process your payment for the current subscription. "
            "To avoid interruption of service, please update your payment information by clicking the link below:\n\n"
            "https://www.netflix.com/YourAccount/Billing\n\n"
            "Thank you for choosing Netflix.\n\n"
            "Netflix Customer Support"
        ),
        "legitimate": False
    },
    {
        "sender": "Google <no-reply@google.com>",
        "recipient": "YourEmail@example.com",
        "subject": "Security Alert: Unusual Sign-In Activity",
        "date": "Sat, 08 Jun 2024 10:10:05 -0700",
        "text": (
            "Hello,\n\n"
            "We detected unusual sign-in activity on your Google account. "
            "If this was you, you can disregard this message. "
            "If you suspect unauthorized access, please secure your account immediately.\n\n"
            "Best,\n"
            "The Google Accounts Team"
        ),
        "legitimate": True
    }

]

# Function to draw text with wraparound and handling newlines
def draw_text(text, font, color, surface, x, y, max_width, max_height):
    lines = text.split('\n')
    y_offset = 0

    for line in lines:
        words = line.split(' ')
        current_line = []

        for word in words:
            current_line.append(word)
            line_width, _ = font.size(' '.join(current_line))
            if line_width > max_width or y_offset > max_height:
                current_line.pop()
                text_surface = font.render(' '.join(current_line), True, color)
                text_rect = text_surface.get_rect(topleft=(x, y + y_offset))
                surface.blit(text_surface, text_rect)
                y_offset += font.get_linesize()  # Increased spacing between lines
                current_line = [word]

        text_surface = font.render(' '.join(current_line), True, color)
        text_rect = text_surface.get_rect(topleft=(x, y + y_offset))
        surface.blit(text_surface, text_rect)
        y_offset += font.get_linesize()  # Increased spacing between lines

# Function to draw styled button
def draw_button(surface, color, rect, text, text_color, font):
    pygame.draw.rect(surface, color, rect, border_radius=15)  # Larger border radius for rounded corners
    shadow_rect = pygame.Rect(rect)
    shadow_rect.inflate_ip(-8, -8)  # Larger shadow offset
    pygame.draw.rect(surface, DARK_GREY, shadow_rect, border_radius=15)  # Larger shadow offset
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=rect.center)
    surface.blit(text_surface, text_rect)

# Define the frame for email text
FRAME_WIDTH = GAME_WIDTH - 40 
FRAME_HEIGHT = GAME_HEIGHT - 100
FRAME_X = (SCREEN_WIDTH - GAME_WIDTH) // 2 + 10
FRAME_Y = (SCREEN_HEIGHT - GAME_HEIGHT) // 2 + 40
frame_rect = pygame.Rect(FRAME_X, FRAME_Y, FRAME_WIDTH, FRAME_HEIGHT)

# Load skull image
skull_image = pygame.image.load("skulls.jpg")
skull_image = pygame.transform.scale(skull_image, (FRAME_WIDTH, FRAME_HEIGHT))

# Define variables to keep track of the current email index
current_email_index = 0
score = 0
# Function to move to the next email
def next_email():
    global current_email_index
    current_email_index = (current_email_index + 1) % len(emails)

# Main game loop
running = True

fill_frame = False
fill_time = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle button clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if answer_button.collidepoint(mouse_pos):
                if emails[current_email_index]["legitimate"]:
                    score += 1
                    print(score)
                else:
                    score -= 5
                    print(score)
                next_email()  
            if delete_button.collidepoint(mouse_pos):
                if not emails[current_email_index]["legitimate"]:
                    score += 1
                    print(score)
                else:
                    score -= 5
                    print(score)
                next_email()  

    # Check if the score is -15
    if score <= -15:
        fill_frame = True
        
    # Draw background image
    screen.blit(background_image, (0, 0))

    #Draw the Email Frame
    if fill_frame:
        pygame.draw.rect(screen, WHITE, frame_rect)
        screen.blit(skull_image, (FRAME_X, FRAME_Y))  # Display skull image
        # Update the display
        pygame.display.flip()
    
        # Wait for 5 seconds
        time.sleep(5)
    
        # Exit the script
        pygame.quit()
        sys.exit()
        

    else:
        pygame.draw.rect(screen, WHITE, frame_rect)

    
    # Draw the email headers
    email_data = emails[current_email_index]
    draw_text(f"From: {email_data['sender']}", header_font, BLACK, screen, FRAME_X + 10, FRAME_Y + 20, FRAME_WIDTH - 20, FRAME_HEIGHT - 20)
    draw_text(f"To: {email_data['recipient']}", header_font, BLACK, screen, FRAME_X + 10, FRAME_Y + 60, FRAME_WIDTH - 20, FRAME_HEIGHT - 60)
    draw_text(f"Subject: {email_data['subject']}", header_font, BLACK, screen, FRAME_X + 10, FRAME_Y + 100, FRAME_WIDTH - 20, FRAME_HEIGHT - 100)
    draw_text(f"Date: {email_data['date']}", header_font, BLACK, screen, FRAME_X + 10, FRAME_Y + 140, FRAME_WIDTH - 20, FRAME_HEIGHT - 140)

    # Draw the email body
    draw_text(email_data['text'], email_font, BLACK, screen, FRAME_X + 10, FRAME_Y + 180, FRAME_WIDTH - 40, FRAME_HEIGHT - 180)

    # Draw buttons
    answer_button = pygame.Rect(SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT - 250, 180, 60)
    delete_button = pygame.Rect(SCREEN_WIDTH // 2 + 0, SCREEN_HEIGHT - 250, 180, 60)

    # Draw the buttons with styling
    draw_button(screen, BLUE, answer_button, "Accept", WHITE, button_font)
    draw_button(screen, RED, delete_button, "Decline", WHITE, button_font)

    # Update the display
    pygame.display.flip()

pygame.quit()
sys.exit()