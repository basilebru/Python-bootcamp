class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if len(coefs) != len(words):
            return(-1)
        res = 0
        for c, w in zip(coefs, words):
            res =  res + c * float(len(w))
        print(res)
        return(res)

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if len(coefs) != len(words):
            print(-1)
            return(-1)
        res = 0
        for i, c in enumerate(coefs):
            res = res + c * float(len(words[i]))
        print(res)

words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 3.0, 1.0, 999.0, 0.5]

Evaluator.zip_evaluate(coefs, words)
Evaluator.enumerate_evaluate(coefs, words)