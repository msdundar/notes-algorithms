# encoding: UTF-8

require 'thread'

@graph = [["alice", "bob", "claire"], ["anuj", "peggy"], ["peggy"], ["thom", "jonny"]]
@search_queue = Queue.new

def enqueue(arr)
  added = []

  arr.each do |item|
    item.each do |element|
      unless added.include?(element)
        @search_queue.push(element)
        added << element
        puts "#{element} queued!"
      end
    end
  end
end

def dequeue(queue)
  until queue.empty?
    item = queue.shift
    puts "#{item} dequeued!"
    sleep 0.5
  end
end

def search(name, queue)
  searched = []

  unless queue.empty? || searched.include?(name)
    if person_is_seller(name)
      puts "#{name} is a mango seller!"
      return true
    else
      searched << name
    end
  end
end

# this function checks whether the person's name ends with the letter m. If it does, they're a mango seller.
def person_is_seller(name)
  name[-1] == 't'
end

enqueue(@graph)
dequeue(@search_queue)
enqueue([["serhat"]])
search("serhat", @search_queue)