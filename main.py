from objc_util import ObjCClass
import pdbg


class Feedback:

  def __init__(self):
    '''
    https://developer.apple.com/documentation/uikit/uiimpactfeedbackgenerator/feedbackstyle
      
      case light = 0
      case medium = 1
      case heavy = 2
      case soft = 3
      case rigid = 4
    '''
    self.__strong = self.__get_feedback_generator(4)
    self.__weak = self.__get_feedback_generator(0)

  @property
  def strong(self):
    return self.__strong.impactOccurred()

  @property
  def weak(self):
    return self.__weak.impactOccurred()

  def __get_feedback_generator(self, style: int = 0) -> ObjCClass:
    """
    call feedback ex:
    `UIImpactFeedbackGenerator.impactOccurred()`
    """

    UIImpactFeedbackGenerator = ObjCClass('UIImpactFeedbackGenerator').new()
    UIImpactFeedbackGenerator.prepare()
    UIImpactFeedbackGenerator.initWithStyle_(style)
    return UIImpactFeedbackGenerator


if __name__ == '__main__':
  feed_back = Feedback()
  feed_back.strong
