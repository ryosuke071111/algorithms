class Tree
  attr_reader :value, :children

  def initialize(v, c =[])
    @value = v
    @children = c
  end

def search(v)
  return true if @value == v
  @children.each {|c|
    return true if c.search(v)
  }
  false
end

end

t1 = Tree.new(1)

t2 = Tree.new(1, [
  Tree.new(2),
  Tree.new(3),
  Tree.new(4),
  Tree.new(5, [Tree.new(6), Tree.new(7)])
  ])

puts t2.search(7)
