from math import factorial as fact

class Bezier:
    def __init__(self, *args, **kwargs):
        if len(args) == 1:
            inp = list(args[0])
            self.x = [i[0] for i in inp]
            self.y = [i[1] for i in inp]
        if len(args) == 2:
            self.x = args[0]
            self.y = args[1]
        if 'step' in kwargs:
            self.step = kwargs['step']
        else:
            self.step = 1e-3
        if 'points' in kwargs:
            self.points = kwargs['points']
        else:
            self.points = False
    
    def __getitem__(self, t):
        def stepper(start, stop, step):
            t = start
            c = (lambda x,y: x>=y) if (start > stop) else (lambda x,y: y>=x)
            while c(t, stop):
                yield t
                t += step
        
        if isinstance(t, slice):
            start = t.start
            step = t.step
            stop = t.stop
            if start is None:
                if step is None or step == 0:
                    step = self.step
                if step > 0:
                    start = 0
                else:
                    start = 1
            if stop is None:
                if step is None or step == 0:
                    step = self.step
                if step > 0:
                    stop = 1
                else:
                    stop = 0
            if step is None or step == 0:
                step = abs(self.step) if stop > start else -abs(step)
            start = max(min(start, 1), 0)
            stop = max(min(stop, 1), 0)
            if self.points:
                return [self[i] for i in stepper(start, stop, step)]
            else:
                pnts = [self[i] for i in stepper(start, stop, step)]
                return [[i[0] for i in pnts], [i[1] for i in pnts]]
        else:
            if not (0 <= t <= 1):
                raise ValueError('t value must be in range [0, 1]')
            n = len(self.x) - 1
            x = 0
            y = 0
            for i in range(n+1):
                #eww
                x += self.x[i]*((1-t)**(n-i))*(t**i)*fact(n)/fact(i)/fact(n-i)
                y += self.y[i]*((1-t)**(n-i))*(t**i)*fact(n)/fact(i)/fact(n-i)
            return (x, y)
