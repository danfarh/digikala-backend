import redis

redis = redis.Redis.from_url('redis://')

def redis_set(name, value, ex):
    return redis.set(name,value,ex)

def redis_get(name):
    value = redis.get(name)
    return value