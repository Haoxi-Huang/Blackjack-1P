#Name: Steve Huang
#Date: January 19, 2015
#File Name: game.py
#Description: The game of Blackjack. The rules are as follows:
#             The overall goal of the game is to get as close to or equal 21
#             without going over
#             1. The player and dealer are dealt two cards.
#             2. If the player gets 'blackjack' (an ace and a 10-card) without
#                the dealer getting blackjack, they win.
#             3. If the dealer gets blackjack without the player getting blackjack,
#                the dealer wins.
#             4. If both the dealer and the player get blackjack, a 'push' or tie
#                occurs.
#             5. If neither the dealer nor the player get blackjack, the player is
#                given a chance to hit to increase their total or stand stay where they are.
#             6. If the player hits, their total increases by that much. If they are over
#                21, they bust and lose to the dealer.
#             7. If the player has 5 cards under or equalling 21, they automatically
#                win. The same applies to the dealer.
#             8. If the player chooses to stand, play switches to the dealer.
#             9. The dealer follows the same rules as the player except they stand on 17.
#             10. Once both sides stand, the dealer and the player compare cards.
#             11. Whoever has the highest total wins! If they have the same total,
#                 they 'push' or tie.

#Import the necessary modules. 
import random
from graphics import *
from button import Button
import time

#Define the needed functions.
#Define the function that draws cards and makes a file name for the drawn card.
def cardDraw(drawnCards):
    
    #Set a flag to repeat the loop if a card has already been drawn.
    cardRepeat = True

    #Loop until a card that has not been drawn is drawn.
    while cardRepeat == True:

        #Set the lists for the suit and the number of a card.
        cardNumList = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        cardSuitList = ['c', 'd', 'h', 's']

        #Randomly generate two numbers to simulate the suit and number.
        cardNum = cardNumList[random.randint(0, 12)]
        cardSuit = cardSuitList[random.randint(0, 3)]

        #Concatenate the suit, the number, and .gif to make a file name.
        card = cardSuit + str(cardNum) + '.gif'

        #If the concatenated card has already been drawn, repeat the loop.
        if drawnCards.count(card) > 2:
            cardRepeat = True

        #If the concatenated card has not been drawn, add it to the drawn card list,
        #and return the card.
        else:
            drawnCards.append(card)
            return card

#Define the function that converts file names used for importing into numbers.
def convertFileNameToNum(cardName):

    #If there is a 10 in the file name, set the numerical value of the card to 10.
    if '10' in cardName:
        cardNum = 10

    #If there is a face card in the file name, set the numerical value of the
    #card to 10.
    elif 'J' in cardName or 'Q' in cardName or 'K' in cardName:
        cardNum = 10

    #If there is an A in the file name, set the value of the card to be A to be
    #dealt with as a special circumstance.
    elif 'A' in cardName:
        cardNum = 'A'

    #For every other file name, set the value of the card to be equal to the number
    #in the file name.
    else:

        #Traverse the file name string.
        for i in cardName:

            #If a given character is a number, set the value of that card
            #to be equal to that number.
            if i.isdigit():
                cardNum = int(i)

    #Return the value of the card.
    return cardNum

#Define the function that displays the total of the player's hand.
def playerTotalTextProperties(playerTotal):

    #Display the total of the player's hand.
    playerTotalText = Text(Point(500, 120), 'Your total is: '+ str(sum(playerTotal)))
    playerTotalText.setFill('orange')

    #Return the properties set in the function.
    return playerTotalText

#Define the function that displays the total of the dealer's hand.
def dealerTotalTextProperties(dealerTotal):

    #Display the total of the dealer's hand.
    dealerTotalText = Text(Point(500, 460), 'Dealer\'s total is: ' + str(sum(dealerTotal)))
    dealerTotalText.setFill('orange')

    #Return the properties set in the function.
    return dealerTotalText

#Define the function that checks for aces in the first card.
def aceCheck(hand, total):
    
    #If an ace is in the first card, check for additional aces.
    if 'A' in hand[0]:

        #If there is a second ace, set the value list to 11 and 1.
        if 'A' in hand[1]:
            total = [11, 1]

        #If there is only one ace at the beginning of the hand, set
        #the value of the ace to be 11.
        else:
            total[0] = 11

    #Return the value list.
    return total

#Define the function that decides the value of a drawn ace after the initial deal.
def aceDraw(numCard, total):

    #If having an 11 would exceed 21, set the ace equal to 1.
    if sum(total[0:(len(total) - 1)]) + 11 > 21:
        total[numCard] = 1

    #If not, set the ace equal to 11. 
    else:
        total[numCard] = 11

    #Return the card's value.
    return total[numCard] 

#Define the function that creates the rules window.
def rulesWindow():

    #Create a window that displays the rules of Blackjack.
    rules = GraphWin("Rules", 540, 400)
    rules.setCoords(0, 0, 540, 400)
    rules.setBackground('White')

    #Print the title of the window.
    title = Text(Point(270, 380), 'Basic Rules of Blackjack')
    title.setStyle('bold')
    title.setTextColor('red')
    title.setSize(16)
    title.draw(rules)

    #Print the main text of the window.
    body = Text(Point(270, 350), '  Blackjack is played with the dealer being dealt two cards and the player being')
    body.draw(rules)
    body = Text(Point(270, 330), 'dealt two cards with the goal to get as close to or equal 21 without going over.')
    body.draw(rules)
    body = Text(Point(270, 310), '  If the dealer or the player get what is called a \'blackjack\', which is a')
    body.draw(rules)
    body = Text(Point(270, 290), 'combination of an ace and a 10-card(10, J, Q, K), he or she wins on the first')
    body.draw(rules)
    body = Text(Point(270, 270), 'turn. If both the dealer and the player get blackjack, a \'push\' or a tie occurs.')
    body.draw(rules)
    body = Text(Point(270, 250), '  If neither the dealer or the player get blackjack, play continues. The player')
    body.draw(rules)
    body = Text(Point(270, 230), 'is given a chance to hit to get closer or equal 21 or stand to maintain their')
    body.draw(rules)
    body = Text(Point(270, 210), 'hand in hopes of beating the dealer. If the player\'s hand total exceeds 21, he')
    body.draw(rules)
    body = Text(Point(270, 190), 'or she \'busts\' and loses to the dealer. If the player has 5 cards and is 21')
    body.draw(rules)
    body = Text(Point(270, 170), 'or less, they win with a 5-card charlie. The same applies to the dealer. Once')
    body.draw(rules)
    body = Text(Point(270, 150), 'the player chooses to stand, play switches to the dealer.')
    body.draw(rules)
    body = Text(Point(270, 130), '  The dealer must also follow the same rules as the player. Once both')
    body.draw(rules)
    body = Text(Point(270, 110), 'sides stand, the dealer and the player compare cards and whoever has the ')
    body.draw(rules)
    body = Text(Point(270, 90), 'highest total wins! If both players have the same total, they \'push\' or tie.')
    body.draw(rules)

    #Create a button that when clicked closes the rules window.
    closeButton = Button(rules, Point(270, 40), 70, 40, 'Got it!')
    closeButton.activate()

    #Get where the user clicked the mouse.
    mouseClick = rules.getMouse()

    #If the user did not click the button, wait on another click.
    while not closeButton.clicked(mouseClick):
        mouseClick = rules.getMouse()

    #Close the rules window.
    rules.close()
    


                            ###MAIN PROGRAM###

#Initialize the variables that carry over from game to game.
playAgain = True
wins = 0
losses = 0
pushes = 0

#Create a window with width = 640 and height = 480 to play Blackjack.
win = GraphWin("Blackjack", 640, 480)
win.setCoords(0, 0, 640, 480)
win.setBackground('dark green')

#Call the function that makes the rules window.
rulesWindow()

#Loop the game until the user decides to quit.
while playAgain == True:

    #Set the empty lists for drawn cards, file names, and numerical values for
    #the player and dealer each playthrough.
    drawnCards = []
    dealer = []
    player = []
    dealerTotal = []
    playerTotal = []

    #Set the variables that control where a card appears and the index of the 
    numCard = 2
    xCoordMultiple = 3

    #Set the flags for all possible winning and losing conditions.
    push = False
    dealerWin = False
    playerWin = False
    dealerBlackjack = False
    playerBlackjack = False
    pushBlackjack = False
    dealerCharlie = False
    playerCharlie = False
    dealerBust = False
    playerBust = False

    #Place the hit, stand, continue, and quit buttons.
    hitButton = Button(win, Point(270, 200), 60, 30, 'Hit')
    standButton = Button(win, Point(370, 200), 60, 30, 'Stand')
    continueButton = Button(win, Point(600, 280), 70, 30, 'Continue')
    quitButton = Button(win, Point(600, 200), 70, 30, 'Quit')

    #Display the text to indicate where the player's cards are.
    playerText = Text(Point(42, 120), 'Player: ')
    playerText.setFill('Orange')
    playerText.draw(win)

    #Display the text to indicate where the dealer's cards are.
    dealerText = Text(Point(42, 460), 'Dealer: ')
    dealerText.setFill('Orange')
    dealerText.draw(win)
    
    #Display the card back in-between the player and the dealer.
    cardDeck = Image(Point(50, 240), 'b2fv.gif')
    cardDeck.draw(win)

    #Display the first line of the scoreboard.
    winLossTotal1 = Text(Point(320, 290), 'Wins - Losses - Pushes')
    winLossTotal1.setFill('red')
    winLossTotal1.draw(win)

    #Display the second line of the scoreboard with wins, losses, and pushes.
    winLossTotal2 = Text(Point(320, 265), str(wins)+ '        ' + str(losses) + '       ' + str(pushes))
    winLossTotal2.setFill('red')
    winLossTotal2.setSize(14)
    winLossTotal2.draw(win)

    #Add two cards to both dealer and player hands to start the game.
    dealer.append(cardDraw(drawnCards))
    dealer.append(cardDraw(drawnCards))
    player.append(cardDraw(drawnCards))
    player.append(cardDraw(drawnCards))

    #Display the first card for the dealer at specified coordinates and
    #delay the displaying of the next card.
    image = Image(Point(50, 400), dealer[0])
    image.draw(win)
    time.sleep(0.3)

    #Display the first card for the player at specified coordinates and
    #delay the displaying of the next card.
    image = Image(Point(50, 60), player[0])
    image.draw(win)
    time.sleep(0.3)

    #Display the second card for the dealer at specified coordinates
    #and delay the displaying of the next card.
    image = Image(Point(130, 400), 'b2fv.gif')
    image.draw(win)
    time.sleep(0.3)

    #Display the second card for the player at specified coordinates.
    image = Image(Point(130, 60), player[1])
    image.draw(win)

    #Convert the file names in the dealer and player card list to numbers.
    for i in range(2):
        dealerTotal.append(convertFileNameToNum(dealer[i]))
        playerTotal.append(convertFileNameToNum(player[i]))

    #If an ace is in the player's first card, check for additional aces.
    if 'A' in player[0]:

        #Call the function that checks for aces if the first card is an ace.
        playerTotal = aceCheck(player, playerTotal)

    #If there is an ace in the second card dealt without the first card being an
    #ace, force it to be worth 11.
    elif 'A' in player[1]:
        playerTotal[1] = 11

    #If an ace is in the dealer's first card, check for additional aces.
    if 'A' in dealer[0]:

        #Call the function that checks for aces if the first card is an ace.
        dealerTotal = aceCheck(dealer, dealerTotal)

    #If there is an ace in the second card dealt without the first card being an
    #ace, force it to be worth 11.
    elif 'A' in dealer[1]:
        dealerTotal[1] = 11

    #Call the function that sets the properties of the player total text,
    #assign it to a variable and draw it to the window.
    playerTotalText = playerTotalTextProperties(playerTotal)
    playerTotalText.draw(win)

    #Set the properties of the dealer total text, assign it to a variable
    #display only the shown card and draw it to the window.
    dealerTotalText = Text(Point(500, 460), 'Dealer\'s total is: ' + str(dealerTotal[0]))
    dealerTotalText.setFill('orange')
    dealerTotalText.draw(win)

    #If the player has blackjack check the dealer's hand.
    if len(player) == 2 and sum(playerTotal) == 21:

        #If the dealer has blackjack at the same time the player has blackjack,
        #declare a push.
        if len(dealer) == 2 and sum(dealerTotal) == 21:

            #Display the dealer's total. Undraw the original text, call the function that
            #sets the properties of the dealer total text, assign it to a variable and
            #draw it to the window.
            dealerTotalText.undraw()
            dealerTotalText = dealerTotalTextProperties(dealerTotal)
            dealerTotalText.draw(win)

            #Display the player's total. Undraw the original text, call the function that
            #sets the properties of the player total text, assign it to a variable and
            #draw it to the window.
            playerTotalText.undraw()
            playerTotalText = playerTotalTextProperties(playerTotal)
            playerTotalText.draw(win)

            #Display the dealer's second card at specified coordinates.
            image = Image(Point(130, 400), dealer[1])
            image.draw(win)

            #Set the push and push blackjack flag to be true.
            pushBlackjack = True
            push == True

        #If the dealer does not have blackjack, declare the player the winner.    
        else:

            #Display the player's total. Undraw the original text, call the function that
            #sets the properties of the player total text, assign it to a variable and
            #draw it to the window.
            playerTotalText.undraw()
            playerTotalText = playerTotalTextProperties(playerTotal)
            playerTotalText.draw(win)

            #Set the player win and player blackjack flags to be true.
            playerBlackjack = True
            playerWin = True

    #If the dealer has blackjack without the player having blackjack, declare
    #the dealer the winner.
    if len(dealer) == 2 and sum(dealerTotal) == 21 and push == False:

        #Display the dealer's second card at specified coordinates.
        image = Image(Point(130, 400), dealer[1])
        image.draw(win)

        #Display the dealer's total. Undraw the original text, call the function that
        #sets the properties of the dealer total text, assign it to a variable and
        #draw it to the window.
        dealerTotalText.undraw()
        dealerTotalText = dealerTotalTextProperties(dealerTotal)
        dealerTotalText.draw(win)

        #Set the dealer win and dealer blackjack flag to be true.
        dealerBlackjack = True
        dealerWin = True

    #While the player has less or equal to 21 and neither the dealer nor the player
    #have won, allow the player to hit or stand.
    while sum(playerTotal) <= 21 and dealerWin == False and playerWin == False:

        #Activate the hit and stand button and wait for a click.
        hitButton.activate()
        standButton.activate()
        click = win.getMouse()

        #Display the player's total. Undraw the original text, call the function that
        #sets the properties of the player total text, assign it to a variable and
        #draw it to the window.
        playerTotalText.undraw()
        playerTotalText = playerTotalTextProperties(playerTotal)
        playerTotalText.draw(win)

        #If the hit button was clicked, draw a card to the player's hand.
        if hitButton.clicked(click):

            #Wait 0.3 seconds to enhance surprise.
            time.sleep(0.3)

            #Add the file name of the drawn card to the player card list.
            player.append(cardDraw(drawnCards))

            #Convert the file name to a number and add it to the player value list.
            #Convert only the card specified by the variable.
            playerTotal.append(convertFileNameToNum(player[numCard]))

            #Draw the card drawn on the screen according to where the variable indicates
            #at a fixed y-coordinate of 60.
            image = Image(Point((80*xCoordMultiple) - 30, 60), player[numCard])
            image.draw(win)

            #If the drawn card was an ace, convert the ace into either an 11 or a 1.
            if playerTotal[numCard] == 'A':

                #Convert the ace based on the player's hand.
                playerTotal[numCard] = aceDraw(numCard, playerTotal)

            #If the player exceeds 21 with the drawn card, check for aces.
            if sum(playerTotal) > 21:

                #Traverse the player value list.
                for i in playerTotal:

                    #If an ace worth 11 is found, remove it and add a 1 to the
                    #player value list.
                    if i == 11:
                        playerTotal.remove(11)
                        playerTotal.append(1)

            #Refresh the player's total text after a card has been drawn. Undraw the
            #original text, call the function that sets the properties of the
            #player total text, assign it to a variable and draw it to the window.
            playerTotalText.undraw()
            playerTotalText = playerTotalTextProperties(playerTotal)
            playerTotalText.draw(win)

            #Add one to the card counter and the placement of the x-coordinate variable.
            numCard += 1
            xCoordMultiple += 1

        #If the stand button is clicked, reset the card counter and the placement
        #of the x-coordinate variable for the dealer's use.
        elif standButton.clicked(click):
            numCard = 2
            xCoordMultiple = 3

            #Deactivate the hit and stand button so they cannot be used during
            #the dealer's turn.
            hitButton.deactivate()
            standButton.deactivate()

            #Break from the player turn loop.
            break

        #If the player has 5 cards and the sum of the player value list is less
        #than or equal to 21, the player wins with a 5-card charlie. 
        if len(playerTotal) == 5 and sum(playerTotal) <= 21:
            hitButton.deactivate()
            standButton.deactivate()

            #Set the player win and player charlie flags to be true.
            playerCharlie = True
            playerWin = True

            #Break from the player turn loop.
            break

    #If the player has a total over 21 after the player turn loop, tell the player
    #that they busted.
    if sum(playerTotal) > 21:

        #Deactivate the hit and stand button after a game.
        hitButton.deactivate()
        standButton.deactivate()

        #Show the player the dealer's second card after they bust.
        image = Image(Point(130, 400), dealer[1])
        image.draw(win)

        #Display the dealer's total. Undraw the original text, call the function that
        #sets the properties of the dealer total text, assign it to a variable and
        #draw it to the window.
        dealerTotalText.undraw()
        dealerTotalText = dealerTotalTextProperties(dealerTotal)
        dealerTotalText.draw(win)

        #Set the player bust and dealer win flags to be true.
        playerBust = True
        dealerWin = True


    #While the sum of the dealer's hand is under 21 and neither the player nor the dealer
    #has won, allow the dealer to play.
    while sum(dealerTotal) <= 21 and dealerWin == False and playerWin == False:

        #Delay the showing of the second card to enhance suspense.
        time.sleep(0.3)

        #Display the dealer's second card.
        image = Image(Point(130, 400), dealer[1])
        image.draw(win)

        #Display the dealer's total. Undraw the original text, call the function that
        #sets the properties of the dealer total text, assign it to a variable and
        #draw it to the window.
        dealerTotalText.undraw()
        dealerTotalText = dealerTotalTextProperties(dealerTotal)
        dealerTotalText.draw(win)

        #If the dealer's hand is worth less than 17, force the dealer to hit.
        if sum(dealerTotal) < 17:

            #Delay the showing of the drawn card to enhance suspense.
            time.sleep(0.3)

            #Add the file name of the drawn card to the dealer card list.
            dealer.append(cardDraw(drawnCards))

            #Convert the file name to a number and add it to the dealer value list.
            #Convert only the card specified by the variable.
            dealerTotal.append(convertFileNameToNum(dealer[numCard]))
            image = Image(Point((80*xCoordMultiple) - 30, 400), dealer[numCard])
            image.draw(win)

            #If the drawn card was an ace, convert the ace into either an 11 or a 1.
            if dealerTotal[numCard] == 'A':

                #Convert the ace based on the dealer's hand.
                dealerTotal[numCard] = aceDraw(numCard, dealerTotal)

            #If the player exceeds 21 with the drawn card, check for aces.
            if sum(dealerTotal) > 21:

                #Traverse the dealer value list.
                for i in dealerTotal:

                    #If an ace worth 11 is found, remove it and add a 1.
                    if i == 11:
                        dealerTotal.remove(11)
                        dealerTotal.append(1)

            #Refresh the dealer's total text after a card has been drawn. Undraw the
            #original text, call the function that sets the properties of the
            #dealer total text, assign it to a variable and draw it to the window.  
            dealerTotalText.undraw()
            dealerTotalText = dealerTotalTextProperties(dealerTotal)
            dealerTotalText.draw(win)

            #If the dealer has 5 cards and the sum of the dealer value list is less
            #than or equal to 21, the dealer wins with a 5-card charlie. 
            if len(dealerTotal) == 5 and sum(dealerTotal) <= 21:

                #Set the dealer charlie and dealer win flags to be true.
                dealerCharlie = True
                dealerWin = True

                #Break out of the dealer turn loop.
                break

            #Add one to the card counter and the placement of the x-coordinate variable.
            numCard += 1
            xCoordMultiple += 1

        #If the dealer's total is over 17, break from the dealer turn loop.
        else:
            break

    #If the dealer's sum is over 21, set the dealer bust and player win flags
    #to be true.
    if sum(dealerTotal) > 21:

        #Set the dealer bust and player win flags to be true.
        dealerBust = True
        playerWin = True

    #If the player and dealer have not won, lost or tied each other, compare their
    #cards.
    if dealerWin == False and playerWin == False and push == False:

        #If the dealer has a greater card total, he wins.
        if sum(dealerTotal) > sum(playerTotal):

            #Display the text of the dealer winning with a higher total.
            resultText = Text(Point(320, 240), 'The dealer has a higher total than you. Dealer wins.')
            resultText.setTextColor('red')
            resultText.draw(win)

            #Add one to the loss counter.
            losses += 1

        #If the player has a greater card total, he or she wins.
        elif sum(playerTotal) > sum(dealerTotal):

            #Display the text of the player winning with a higher total.
            resultText = Text(Point(320, 240), 'You have a higher total than the dealer. You win!')
            resultText.setTextColor('red')
            resultText.draw(win)

            #Add one to the win counter.
            wins += 1

        #If both the dealer and the player have the same card total, they push.
        else:

            #Display the text of the push.
            resultText = Text(Point(320, 240), 'You and the dealer have the same total. Push!')
            resultText.setTextColor('red')
            resultText.draw(win)

            #Add one to the push counter.
            pushes += 1

    #If the dealer gets blackjack without a player blackjack, display the text
    #of the dealer winning with blackjack.
    if dealerBlackjack:

        #Display the text that shows the result of the dealer beating the player
        #with blackjack.
        resultText = Text(Point(320, 240), 'The dealer has blackjack. You have lost.')
        resultText.setTextColor('red')
        resultText.draw(win)

        #Add one to the loss counter.
        losses += 1

    #If the player gets blackjack without a dealer blackjack, display the text of
    #the player winning with blackjack.
    elif playerBlackjack:

        #Display the text that shows the result of the player beating the
        #dealer with blackjack.
        resultText = Text(Point(320, 240), 'You have blackjack! You have won!')
        resultText.setTextColor('red')
        resultText.draw(win)

        #Add one to the win counter.
        wins += 1

    #If the player and dealer both get blackjack, display that a push has occurred.
    elif pushBlackjack:

        #Display the text that shows the result of the player and dealer
        #tied with both having blackjack.
        resultText = Text(Point(320, 240), 'You and the dealer both have blackjack. Push!')
        resultText.setTextColor('red')
        resultText.draw(win)

        #Add one to the push counter.
        pushes += 1

    #If the dealer has a 5-card Charlie, display the text of the dealer
    #winning with that.
    elif dealerCharlie:
        
        #Display the result of the dealer having a 5-card Charlie.
        resultText = Text(Point(320, 240), 'Dealer has a 5-card Charlie. You lose.')
        resultText.setTextColor('red')
        resultText.draw(win)

        #Add one to the loss counter.
        losses += 1

    #If the player has a 5-card Charlie, display the text of the player
    #winning with that.
    elif playerCharlie:

        #Display the result text of the player winning with a five-card Charlie.
        resultText = Text(Point(320, 240), 'You have a 5-card Charlie. You win!')
        resultText.setTextColor('red')
        resultText.draw(win)
        
        #Add one to the win counter.
        wins += 1

    #If the player busts, display that they bust.
    elif playerBust:

        #Display the result text of the player busting.
        resultText = Text(Point(320, 240), 'You busted!')
        resultText.setTextColor('red')
        resultText.draw(win)

        #Add one to the loss counter.
        losses += 1

    #If the dealer busts, display that the dealer busted.
    elif dealerBust:

        #Display the result text of the dealer busting.
        resultText = Text(Point(320, 240), 'Dealer busted!')
        resultText.setTextColor('red')
        resultText.draw(win)

        #Add one to the win counter.
        wins += 1

    #Activate the continue and quit buttons for the user to decide what to do.
    continueButton.activate()
    quitButton.activate()

    #Wait on their mouse click.
    click = win.getMouse()

    #If the user does not hit the quit button, check if they hit the continue button.
    while not quitButton.clicked(click):

        #If the user hits the continue button, reset the game screen.
        if continueButton.clicked(click):

            #Draw a background coloured triangle over the player's cards.
            clearPlayerCards = Rectangle(Point(10, 10), Point(600, 110))
            clearPlayerCards.setFill('dark green')
            clearPlayerCards.setOutline('dark green')
            clearPlayerCards.draw(win)

            #Draw a background coloured triangle over the dealer's cards.
            clearDealerCards = Rectangle(Point(10, 470), Point(600, 320))
            clearDealerCards.setFill('dark green')
            clearDealerCards.setOutline('dark green')
            clearDealerCards.draw(win)

            #Undraw the result text, the player's total text, the dealer's total
            #text, and the scoreboard.
            resultText.undraw()
            playerTotalText.undraw()
            dealerTotalText.undraw()
            winLossTotal1.undraw()
            winLossTotal2.undraw()

            #Set the play again flag to be true to play the game again.
            playAgain = True

            #Break out of the event loop.
            break

        #Wait on the user if they did not hit either the continue or quit button.
        click = win.getMouse()

    #If the user decides to quit, set the play again flag to be false to stop the game.
    #Close the window.
    if quitButton.clicked(click):
        playAgain = False
        win.close()

