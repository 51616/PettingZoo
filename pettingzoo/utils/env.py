class AECEnv(object):
    def __init__(self):
        pass

    def step(self, action, observe=True):
        raise NotImplementedError

    def reset(self, observe=True):
        raise NotImplementedError

    def observe(self, agent):
        raise NotImplementedError

    def last(self):
        raise NotImplementedError("last() has been removed. Please use final() instead.")

    def render(self, mode='human'):
        raise NotImplementedError

    def close(self):
        pass

    def agent_iter(self, max_agent_iter=2**63):
        return AECIterable(self, max_agent_iter)


class AECIterable:
    def __init__(self, env, max_agent_iter):
        self.env = env
        self.max_agent_iter = max_agent_iter

    def __iter__(self):
        if getattr(self.env, "_has_updated", None) is None:
            return AECIterator(self.env, self.max_agent_iter)
        else:
            return AECOrderEnforcingIterator(self.env, self.max_agent_iter)


class AECIterator:
    def __init__(self, env, max_agent_iter):
        self.env = env
        self.iters_til_term = max_agent_iter
        self._was_done = False

    def __next__(self):
        if all(self.env.dones.values()) or self.iters_til_term <= 0:
            raise StopIteration
        self.iters_til_term -= 1
        return self.env.agent_selection


class AECOrderEnforcingIterator(AECIterator):
    def __next__(self):
        agent = super().__next__()
        assert self.env._has_updated, "need to call step() or reset() in a loop over `agent_iter`!"
        self.env._has_updated = False
        return agent
