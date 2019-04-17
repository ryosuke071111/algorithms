class List
  def initialize
    @cdr = nil #値
    @car = nil #次の要素へのラベル
  end
  attr_accessor :cdr, :car

  def add_last(x)
    a = self
    a = a.car until a.car.nil? #ポイントがからの値まで進む
    a.car = List.new #ポインタにインスタンス作成
    a.car.cdr = x     #その値に引数を代入
  end

  def size
    a = self
    i = 0
    i += 1 while a = a.car #ポインタの先端に行くまで数える
    return i
  end

  def each
    a = self.car
    self.size.times do    #サイズ分繰り返し
      yield a.cdr         #現時点の値を出力
      a = a.car           #現時点をポインタの値にする
    end
  end
end

z = List.new
z.add_last('ringo')
z.add_last('orange')
z.add_last('suica')
z.add_last('melon')
z.add_last('ichigo')

puts z.size

z.each do |i|
  puts i
end
