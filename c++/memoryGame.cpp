// Memory game

/*
For this part, add a second player to the game. Make sure you are not duplicating code. If you
find that you are duplicating code, refactor. Also set up a scoring system that keeps track of each
player’s matches. Remember that the players will want to be able to see the scores as the game
progresses. To test, you will need to keep track of the score for each player yourself and verify
that the code is keeping track correctly. Write a test plan that describes your testing strategy even
if you cannot specify exact inputs and outputs.*/

#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <ctime>
#include <string>
#include <locale>

using namespace std;

//declare constants
const int NUMBER_OF_ROWS = 4;
const int NUMBER_OF_COLS = 4;
const char LIST_OF_COLUMNS [] = {' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
const int NUMBER_OF_PLAYERS = 2;
int playerOneScore = 0;
int playerTwoScore = 0;
bool gameOn = true;

// delcare card struct
struct card {
  int value;
  bool faceUp;
};

//delcare functions
void initializeBoard(card board[NUMBER_OF_ROWS][NUMBER_OF_COLS], bool value);
void displayBoard(card board[NUMBER_OF_ROWS][NUMBER_OF_COLS]);
void testMode(card board[NUMBER_OF_ROWS][NUMBER_OF_COLS]);
void playersTurn(card board[NUMBER_OF_ROWS][NUMBER_OF_COLS]);
void getCards (card board[NUMBER_OF_ROWS][NUMBER_OF_COLS], int current_player);
void handleMatch(card board[NUMBER_OF_ROWS][NUMBER_OF_COLS], int rowInOne, int colInOne, int rowInTwo, int colInTwo, int current_player);
void playerScore(int current_player);
bool gameOver(card board[NUMBER_OF_ROWS][NUMBER_OF_COLS],string nameOne, string nameTwo);

int main() {
  card board[NUMBER_OF_ROWS][NUMBER_OF_COLS];
  testMode(board);
};

/*
The test plan would specify that you play the game to completion. Add logic to your program so
that you can run in “test mode” where the initial state of the board is revealed, and “play mode”
where the initial state of the board is hidden. In your test plan, specify how to turn “test mode”
on or off.
*/
void testMode(card board[NUMBER_OF_ROWS][NUMBER_OF_COLS]){
  bool enableTestMode = false;
  cout << "Enable testmode? 1 or 0: ";
  cin >> enableTestMode;
  if(enableTestMode){
    initializeBoard(board, true);
    displayBoard(board);
    initializeBoard(board, false);
    playersTurn(board);
  } else {
    initializeBoard(board, false);
    displayBoard(board);
    playersTurn(board);
  }
};
// function random rumbers to 4x4 matrix which later be printed from displayBoard
// void initializeBoard(card board[NUMBER_OF_ROWS][NUMBER_OF_COLS], bool value) // unit test change
void initializeBoard(card board[NUMBER_OF_ROWS][NUMBER_OF_COLS],bool value) {
  // array for used numbers for random number 1-8 in pairs
  int isUsedNumber[16] = {1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8};
  // Initialize random number generator
  srand((unsigned)time(NULL));
  //start loop for rows and cols
  for (int rows = 0; rows < NUMBER_OF_ROWS; rows++){
    for (int cols= 0; cols < NUMBER_OF_COLS; cols++){
      // set faceUp boolen to false for each itiriation of rows and cols
      board[rows][cols].faceUp = value;
      // generat a random number between the constants and 1
      int randNumber = rand()%(NUMBER_OF_ROWS * NUMBER_OF_COLS)+1;
      // while current index of isUsedNumber = 0 generate another randNumber
      while(isUsedNumber[randNumber - 1] == 0){
        randNumber = rand()%(NUMBER_OF_ROWS * NUMBER_OF_COLS)+1;
      }
      // assign isUsedNumber indexed value to the current rows cols index
      board[rows][cols].value = isUsedNumber[randNumber - 1];
      // set current isUsedNumber index value to 0
      isUsedNumber[randNumber - 1] = 0;
    }
  }
};

// function that take the board stucture as input and displays board
void displayBoard(card board[NUMBER_OF_ROWS][NUMBER_OF_COLS]){
  // loop through the array letters list to total number of cols delcared
  for (int letter = 0; letter <= NUMBER_OF_COLS; letter++)
  cout << setw(2) << LIST_OF_COLUMNS[letter];
  cout << "\n";
  // loop and print "-" to total number of cols delcared
  for (int i = 0; i <= NUMBER_OF_COLS; i++)
    cout << setw(2) << "-";
    cout << endl;
  //start loop for rows and cols to display the [NUMBER_OF_ROWS][NUMBER_OF_COLS] matrix to the player
  for (int rows = 0; rows < NUMBER_OF_ROWS; rows++){
    cout << setw(1) << rows +1 << "|";
    for (int cols = 0; cols < NUMBER_OF_COLS; cols++)
      // show the value of the current [rows][cols] value if the current [rows][cols] boolen faceUp is true
      if(board[rows][cols].faceUp){
        cout << setw(2) << board[rows][cols].value;
      } else {
        cout << setw(2) << "*";
      }
      cout << endl;
  }
  cout<<endl;
};

void playersTurn(card board[NUMBER_OF_ROWS][NUMBER_OF_COLS]){
  int players;
  int current_player = 1;
  string nameOne, nameTwo;
  cout << "Number of players: ";
  cin >> players;
  while(players > 2 ){
    cout << "Currently only designed for 2 for players, Enter '2' for players: ";
    cin >> players;
  }
  // chcking if there are more than one play enable section of code
  if(players > 1){
    // get names from users to display later
    cout << "Enter name of player 1: ";
    cin >> nameOne;
    cout << "Enter name of player 2: ";
    cin >> nameTwo;
    //set current player to 1 inide of scope outside of loop
    current_player = 1;
    for (int rows = 0; rows < NUMBER_OF_ROWS; rows++){
      for (int cols= 0; cols < NUMBER_OF_COLS; cols++){
        // while there are still faceupcards continue to ask questions
        while(!board[rows][cols].faceUp && gameOn){
          //display current player and then disaply board then ask for user to getCards
          cout << "CURRENT PLAYER: "<< ( current_player == 1 ? nameOne : nameTwo ) << "\n";
          displayBoard(board);
          getCards(board, current_player);
          gameOver(board,nameOne,nameTwo);
          // swtich players at the end of each turn
          if( current_player == 1 ) current_player = 2 ; else current_player = 1;
        }
      }
    }
  }
  // while this is true keep asking questions, this will turn into function for gameOver()
  while(gameOn){
    getCards(board, current_player);
    gameOver(board,nameOne,nameTwo);
  }
};

// function takes the board structure as an input and asks the player to select two cards on the board.
void getCards(card board[NUMBER_OF_ROWS][NUMBER_OF_COLS], int current_player){
  int rowInOne, rowInTwo;
  char colInOneChar, colInTwoChar;
  // used for touppercase loop in case user uses a loewercasd letter for matrix cordinates
  locale loc;
  // get input from user
  cout << "Enter two cordinates for example: A 1 B 1: ";
  cin >> colInOneChar >> rowInOne >> colInTwoChar >> rowInTwo;

  // to uppercase [ 'A', 'Z' ]
  if (colInOneChar >= 'a') colInOneChar -= 32;
  if (colInTwoChar >= 'a') colInTwoChar -= 32;
  int colInOne = colInOneChar - 'A';
  int colInTwo = colInTwoChar - 'A';

  // Convert to 0-based index
  rowInOne--;
  rowInTwo--;

  // Check 1: bound checking
  // printf("Card one: row = %d, col = %d\n", rowInOne, colInOne);
  // printf("Card two: row = %d, col = %d\n", rowInTwo, colInTwo);

  if ( colInOne < 0 || colInOne >= NUMBER_OF_COLS
    || colInTwo < 0 || colInTwo >= NUMBER_OF_COLS
    || rowInOne < 0 || rowInOne >= NUMBER_OF_ROWS
    || rowInTwo < 0 || rowInTwo >= NUMBER_OF_ROWS
  ) {
    cout << "HEY THAT IS AN OUT OF BOUND INPUT, TRY AGAIN MATE!\n";
    getCards(board,current_player);
    return;
  }
  // Check 2: same card checking
  if (colInOne == colInTwo && rowInOne == rowInTwo) {
    cout << "HEY THAT'S THE SAME CARD! TRY AGAIN MATE!\n";
    getCards(board,current_player);
    return;
  }
  // Check 3: already faced up checking
  card& cardOne = board[rowInOne][colInOne];
  card& cardTwo = board[rowInTwo][colInTwo];
  if (cardOne.faceUp || cardTwo.faceUp) {
    cout << "HEY THAT ONE IS ALREADY FACED UP, TRY AGAIN MATE!\n";
    getCards(board,current_player);
    return;
  }
  // Face 'em up
  cardOne.faceUp = true;
  cardTwo.faceUp = true;
  // Only after the input has been validated, use that input to set the state of the selected cards to face up and display the board so the players can see the selections.
  handleMatch(board, rowInOne, colInOne, rowInTwo, colInTwo, current_player);
};

// function  takes the board structure and the selected locations as inputs.
void handleMatch(card board[NUMBER_OF_ROWS][NUMBER_OF_COLS], int rowInOne, int colInOne, int rowInTwo, int colInTwo, int current_player){
  card& cardOne = board[rowInOne][colInOne];
  card& cardTwo = board[rowInTwo][colInTwo];
  // checks for matching values if they match then display board, and add points to playersscores
  if (cardOne.value == cardTwo.value){
    // check for current player and add point to current players' score
    if(current_player == 1) playerOneScore++; else playerTwoScore++;
    printf("Players Score: PlayerOne = %d, PlayerTwo = %d\n", playerOneScore, playerTwoScore);
  } else {
    // else not the same change faceup to false and then disaplyboard for next match
    cout << "NOPE THEY ARE NOT THE SAME\n";
    cardOne.faceUp = false;
    cardTwo.faceUp = false;
    printf("Players Score: PlayerOne = %d, PlayerTwo = %d\n", playerOneScore, playerTwoScore);
  }
};

bool gameOver(card board[NUMBER_OF_ROWS][NUMBER_OF_COLS], string nameOne, string nameTwo){
  if(playerOneScore + playerTwoScore == 8)
  gameOn = false;
  if(playerOneScore > playerTwoScore){
    cout << "Game Over " << nameOne << " Winner! " << playerOneScore;
  }else if(playerOneScore < playerTwoScore){
    cout<< "Game Over " << nameOne << " Winner! " << playerTwoScore;
  }else if (playerOneScore == playerTwoScore){
    cout<< "Game Over " << "It's a Tie";
  }
  return gameOn;
}
