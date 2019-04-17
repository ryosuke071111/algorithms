#クラス定義
class BinarySearchTree
  @@empty = BinarySearchTree.new()
  attr_accessor :value, :left, :right

  def initialize(v, l=@@empty, r=@@empty)
    @value = v
    @left = l
    @right = r
  end

  def search(v)
    ## 自分が@@emptyの場合最下部にいる
    return @@empty if self == @@empty
    return self if @value ==v
    ##入力のが小さければ左へ
    if v < @value
      @left.search(v)
    else
    ##入力のが大きければ右へ
      @right.search(v)
    end
  end

  def add(v)
    return self.class.new(v) if self == @@empty
    if v < @value
      @left =  @left.add(v)
    else
      @right = @right.add(v)
    end
    self
  end

  @t2 = BinarySearchTree.new(1,
              BinarySearchTree.new(2, 3, 7),
                  BinarySearchTree.new(11)
      )

  p @t2.add(12)
end


