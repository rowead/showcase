#!/bin/bash
apt-get install -y ant git-core texinfo

cd /tmp
wget https://artifacts.elastic.co/downloads/logstash/logstash-6.0.0-alpha2.tar.gz
tar xzf logstash-6.0.0-alpha2.tar.gz

mv logstash-6.0.0-alpha2 /opt/logstash-6.0.0-alpha2

ln -s /opt/logstash-6.0.0-alpha2 /opt/logstash
mkdir -p /etc/logstash/conf.d

git clone https://github.com/jnr/jffi.git
cd jffi
ant jar
cp build/jni/libjffi-1.2.so /opt/logstash-6.0.0-alpha2/vendor/jruby/lib/jni/arm-Linux/