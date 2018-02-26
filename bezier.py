class Bezier:
    def __init__(self, *args, **kwargs):
        if len(args) == 1:
            inp = list(args)
            self.x = [i[0] for i in inp]
            self.y = [i[1] for i in inp]
        if len(args) == 2:
            self.x = args[0]
            self.y = args[1]
        else:
            #TODO find proper exception
            raise RuntimeError('')
        if 'step' in kwargs:
            self.step = kwargs[step]
        else:
            self.step = 1e-3
    
    def __getitem__(self, t):
        def stepper(start, stop, step):
            t = start
            c = lambda x,y: x>y if stop > start else lambda x,y: y>x
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
                step = abs(self.step) if stop > step else -abs(step)
            start = min(start, 1)
            start = max(start, 0)
            stop = min(stop, 1)
            stop = max(stop, 0)
        