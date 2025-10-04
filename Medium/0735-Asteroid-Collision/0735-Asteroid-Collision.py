class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        final = []
        estado = ""

        for ast in asteroids:
            estado = ""
            while final and final[-1] > 0 and ast < 0:

                if abs(final[-1]) < abs(ast):
                    final.pop()

                elif abs(final[-1]) == abs(ast):
                    final.pop()
                    estado = "dead"
                    break

                elif abs(final[-1]) > abs(ast):
                    estado = "dead"
                    break

            if estado != "dead":
                final.append(ast)

        return final








