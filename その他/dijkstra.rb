#!ruby
#Last Updated at 04/29/2016

#Skew Heap
#ストアするデータは<=>で比較可能でなければならない

class SkewHeapNode
    attr_accessor :element, :left, :right, :parent
    def initialize(element, left = nil, right = nil)
        @element = element
        @left = left
        @right = right
        @parent = nil
    end
end

class SkewHeap
    attr_reader :size, :root
    def initialize
        @root = nil
        @size = 0
        @position = {}
        @id = 0
    end

    def add(element)
        @id += 1
        @size += 1
        node = SkewHeapNode.new(element)
        @position[@id] = node
        @root = merge(@root, node)
        @id
    end

    def pop
        return nil if @size==0
        @size -= 1
        element = @root.element
        @root = merge(@root.left, @root.right)
        @root.parent = nil if @root
        element
    end

  def change_key(target_id, new_element)
    node = @position[target_id]
    return nil unless node
    if heap_order_property_satisfied?(node, new_element)
        node.element = new_element
    else
        temp = merge(node.left, node.right)
        temp.parent = node.parent if temp
            if node.parent
            if node.parent.left == node
                node.parent.left = temp
            else
                node.parent.right = temp
            end
        else
            @root = temp
        end
        node.element = new_element
        node.left = nil
        node.right = nil
        node.parent = nil

        @root = merge(@root, node)
        @root.parent = nil if @root
    end
    self
  end

  def empty?
    @size == 0
  end

  alias :push :add
  alias :<< :add
  alias :length :size

private
    #p's parent is never changed
    #O(log n)-expected time
    def merge(p, q)
        return p if q.nil?
        return q if p.nil?
        p, q = q, p if p.element > q.element
        q.parent = p
        p.right = merge(p.right, q)
        p.right, p.left = p.left, p.right
        p
    end

    def heap_order_property_satisfied?(node, new_element)
        if node.parent
            return false if node.parent.element > new_element
        end
        if node.left
            return false if node.left.element < new_element
        end
        if node.right
            return false if node.right.element < new_element
        end
        true
    end

    a = SkewHeap.new
    a.add(2)
    a.add(5)
    puts(a.id[0])
end
