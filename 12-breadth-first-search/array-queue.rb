# encoding: UTF-8

require 'thread'

@queue = Queue.new

def produce
  (1..10).each do |i|
    sleep 0.2
    @queue << i
    puts "#{i} enqueued!"
  end
end

def consume
  @queue.close if @queue.empty?

  until @queue.empty?
    sleep 0.3
    value = @queue.shift
    puts "#{value} dequeued!"
  end
end

produce
consume
