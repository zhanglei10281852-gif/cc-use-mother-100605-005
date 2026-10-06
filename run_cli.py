from safety_duty.core import Hazard, summarize


if __name__ == "__main__":
    record = Hazard.create("demo", "v1", "draft", "operator", {"场景": "登记隐患并生成责任摘要"})
    print(summarize(record))

