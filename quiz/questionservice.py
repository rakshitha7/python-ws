from questions import Question
class QuestionService:
    questions=[]
    @classmethod
    def loadQuestion(cls):
        with open("questions.txt") as file:
            data=file.readlines()
            for line in data:
                q = line.split()
                cls.questions.append(Question(*q))

    @classmethod
    def begin_quiz(cls):
        cls.loadQuestion()
        print(f"total question found:{len(cls.question)}")
        num_correct=0
        num_wrong=0
        for i,question in enumerate(cls.question):
            print(f"{i+1}.{question}")
            ch=input("enter your choice [A,B,C,D] only...")
            if ch==question.canswer.strip():
                num_correct +=1
            else:
                num_wrong +=1
            cls.show_result(num_correct,num_wrong)


    @classmethod
    def show_result(cls):
        print("*"*50)
        total_q=len(cls.question)
        print(f"total question:{total_q}")
        print(f"no of  question corect:{num_correct}")
        print(f"no of  question wrong:{num_wrong}")
        percentage=((num_correct)/total_q)*100
        if percentage>=65:
            print("congratulation")
        else:
            print("better luck next time")



