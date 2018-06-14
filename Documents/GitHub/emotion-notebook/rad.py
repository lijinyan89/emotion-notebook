# coding:utf-8

import random

def rand():
    encourage = ["别忘了对自己微笑。",
                "做自己喜欢的事。",
                "快乐，捡起来就是了，随时随地。",
                "生命多远多变，没有必走的路，也没有永恒的局。",
                "做回我自己，向自己的感觉和情绪负责任。",
                "不安是给人生添彩的一点香料。",
                "所有恐惧都是修炼的工具。",
                "学会接受“足够好”（good enough)的状态。"]

    encour = encourage[random.randint(0,len(encourage)-1)]
    return encour
