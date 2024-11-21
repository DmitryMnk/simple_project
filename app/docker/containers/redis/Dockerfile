FROM redis:7.4-alpine

ARG REDIS_USER=${REDIS_USER}
ENV REDIS_USER ${REDIS_USER}

ARG REDIS_PASSWORD=${REDIS_PASSWORD}
ENV REDIS_PASSWORD ${REDIS_PASSWORD}

ARG REDIS_HOST=${REDIS_HOST}
ENV REDIS_HOST ${REDIS_HOST}

ARG REDIS_PORT=${REDIS_PORT}
ENV REDIS_PORT ${REDIS_PORT}

RUN mkdir -p /usr/local/etc/redis && \
    echo "user default off ~* +@all >$REDIS_PASSWORD" > /usr/local/etc/redis/users.acl && \
    echo "user $REDIS_USER on ~* +@all >$REDIS_PASSWORD" >> /usr/local/etc/redis/users.acl


ENTRYPOINT sh -c "redis-server /usr/local/etc/redis/redis.conf --requirepass ${REDIS_PASSWORD} --bind ${REDIS_HOST} --port ${REDIS_PORT}"
