// C++ code
//
int centerIR;
int leftIR;
int rightIR;

int leftFlag;
int centerFlag;
int rightFlag;

//Declare all the functions being used here:
void moveRight();
void moveLeft();
void moveforward();
void moveInreverse();
void setup()
{
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
}

void loop()
{
  // put your main code here, to run repeatedly:
  centerIR = analogRead(A0);
  leftIR = analogRead(A1);
  rightIR = analogRead(A2);

  if (leftIR < 200)
  {
    leftFlag = 1;
  }
  else
  {
    leftFlag = 0;
  }

 if (rightIR < 200)
  {
    rightFlag = 1;
  }
   else
  {
    rightFlag = 0;
  }

  if (centerIR < 200)
  {
    centerFlag = 1;
  }
  else
  {
    centerFlag = 0;
  }

  if ((leftFlag == 1) || (rightFlag == 1) || (centerFlag == 1))
  {

    if (centerFlag == 1)
    {
      if (leftFlag == 1)
      {
        moveRight();
      }

      else if (rightFlag == 1){
        moveLeft();
      } else{
        moveLeft();}
    }
    else if (leftFlag == 1)
    {
      moveRight();
    }
    else if (rightFlag == 1)
    {
      moveLeft();
    }
    else
    {
      moveLeft();
    }
  }

 else
  {
    moveforward();
  }
}

//Function definitions go here:
void moveInreverse()
{
  digitalWrite(10,HIGH);
}

void moveRight()
{
  digitalWrite(13,HIGH);
}

void moveLeft()
{
  digitalWrite(9,HIGH);  
}

void moveforward()
{
  digitalWrite(11,HIGH);
}