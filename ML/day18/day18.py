import tensorflow as tf
import numpy as np

#---------------
class Day18:
    def __init__(self):
        print("Welcome to TensorFlow")

    def qa1(self):
        a = tf.zeros((2,2))
        print(a)
        ses = tf.Session()
        r1 = ses.run(a)
        print(r1)

    def qa2(self):
        X  = tf.constant([[1,2,3],[4,5,6]])
        print(X)
        ses = tf.Session()
        r1 = ses.run(X)
        print(r1)
        #========Create same of X====
        y = tf.zeros(X.shape)
        print("***********")
        print(y.shape)
        ses = tf.Session()
        r2 = ses.run(y)
        print(r2)
        
    def qa3(self):
        a = tf.ones((2,2))
        print(a)
        ses = tf.Session()
        r1 = ses.run(a)
        print(r1)


    def qa4(self):
        X  = tf.constant([[1,2,3],[4,5,6]])
        print(X)
        ses = tf.Session()
        r1 = ses.run(X)
        print(r1)
        #========Create same of X====
        y = tf.ones(X.shape)
        print("***********")
        print(y.shape)
        ses = tf.Session()
        r2 = ses.run(y)
        print(r2)

        
    def qa5(self):
        X = tf.fill((3,2),5)
        print(X)
        ses = tf.Session()
        r2 = ses.run(X)
        print(r2)

    def qa6(self):
         X  = tf.constant([[1,3,5],[4,6,8]], dtype = tf.float32)
         print(X)
         ses = tf.Session()
         r2 = ses.run(X)
         print(r2)

    def qa7(self):
         X  = tf.constant([[1,2,3],[4,6,8]], dtype = tf.float32)
         y = tf.zeros(X.shape)
         print(y)
         ses = tf.Session()
         r2 = ses.run(y)
         print(r2)

    def qa8(self):
        X = tf.linspace(5.0, 10.0, 50, name="linspace")
        ses = tf.Session()
        r2 = ses.run(X)
        print(r2)

    def qa9(self):
        X = tf.random_normal([3, 2], mean=0, stddev=2)
        ses = tf.Session()
        r2 = ses.run(X)
        print(r2)

    def qa10(self):
        X = tf.random_normal([3, 2])
        ses = tf.Session()
        r2 = ses.run(X)
        print(r2)
    def qa11(self):
        # Shuffle the first dimension of a tensor
        X  = tf.constant([[1,2],[3,4],[5,6]], dtype = tf.float32)
        shuff = tf.random_shuffle(X)
        ses = tf.Session()
        r2 = ses.run(shuff)
        print(r2)

    def qa12(self):
        s = np.random.uniform(0,1,300)
        sr = s.reshape(10,10,3) #Reshape in 10 times 10 rows  and 3 columns
        X  = tf.constant(sr, dtype = tf.float32)
        out = tf.random_crop(X,[5,5,3])
        ses = tf.Session()
        r2 = ses.run(out)
        print(r2)
        
    def qa13(self):
        X = tf.constant([[-1,-2,-3],[0,1,2]], dtype = tf.float32)
        y = tf.zeros(X.shape)
        ses = tf.Session()
        r2 = ses.run(y)
        result = tf.not_equal(X, y)
        print(result)

    def qa14To18(self):
        x  = tf.constant([[1,2],[3,4]], dtype = tf.float32)
        y  = tf.constant([[10,20],[30,40]], dtype = tf.float32)
        z  = tf.constant([[2,4],[6,8]], dtype = tf.float32)
        r1 = tf.add(x, y, name="add")
        r2 = tf.subtract(x, y, name="subtract")
        r3 = tf.multiply(x, y, name="Multyply")
        r4 = x * 5;
        rs = tf.add(x,y, name="Mult")
        r5 = tf.add(rs,z, name="add2")
        ses = tf.Session()
        #result = ses.run(r1)
        #result = ses.run(r2)
        #result = ses.run(r3)
        #result = ses.run(r4)
        result = ses.run(r5)
        print(result)
        
    def qa19(self):
       a = tf.constant(51)
       b = tf.constant(15)
       c = tf.add(a,b, name="add")
       sess = tf.Session()
       out = sess.run(c)
       print(out)
       writer = tf.summary.FileWriter('./tb1',sess.graph)
       writer.close()
       sess.close()

    def qa20(self):
        w = tf.constant(1.0, name ="weight")
        print(w)
        sess = tf.Session()
        out = sess.run(w)
        print(out)
        sess.close()

    def qa21(self):
        x = tf.constant(1.0, name ="x")
        y = tf.constant(3.0, name ="y")
        z = tf.constant(5.0, name ="z")
        result = tf.add_n([x, y, z])
        sess = tf.Session()
        out = sess.run(result)
        print(out)
        sess.close()

    def qa22(self):
        p1 = tf.placeholder(tf.float32)
        print p1
      
    def qa23(self):
        p1 = tf.placeholder(tf.float32)
        p2 = tf.placeholder(tf.float32)
        p3 = tf.placeholder(tf.float32)
        psum = tf.add_n([p1,p2,p3])
        sess = tf.Session()
        #out = sess.run(tf.global_variable_initializers())
        out = sess.run(psum, feed_dict = {p1:10,p2:20,p3:60})
        print(out)
        #sess.close()
        
        
        
        
        
        
    
        


s1 = Day18()
#s1.qa1()
#s1.qa2()
#s1.qa3()
#s1.qa4()
#s1.qa5()
#s1.qa6()
#s1.qa7()
#s1.qa8()
#s1.qa9()
#s1.qa10()
#s1.qa11()
#s1.qa12()
#s1.qa13()
#s1.qa14To18()
#s1.qa19()
#s1.qa20()
s1.qa21()
#s1.qa22()
#s1.qa23()


