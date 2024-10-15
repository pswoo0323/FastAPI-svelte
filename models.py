from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)

class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    question_id = Column(Integer, ForeignKey("question.id"))# 답변을 질문과 연결하기 위해
    # 'question.id'는 question 테이블의 id 컬럼을 의미
    question = relationship("Question", backref="answers")
    # 답변 모델에서 질문 모델을 참조하기 위해 추가
    # 답변 객체(예: answer)에서 연결된 질문의 제목을 answer.question.subject처럼 참조할 수 있다