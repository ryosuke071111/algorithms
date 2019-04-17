class BinaryTree
  attr_reader :value, :left, :right

  def initialize(v, l=nil, r=nil)
    @value = v
    @left = l
    @right = r
  end
end



def search(v)
  # 自身と一致してたら true を返す
  return true if @value == v

  # 左の子以下に見つかれば true
  return true if @left != nil and @left.search(v)

  # 右の子以下に見つかれば true
  return true if @right != nil and @right.search(v)
  # 何処にもなかった
  false
end

@a = BinaryTree.new(1, @b = BinaryTree.new(2, 3, 4), @c = BinaryTree.new(5,6,7))

puts @b.search(4)
