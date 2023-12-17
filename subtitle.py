# class Subtitle():

    
#     def __init__(self, strPlotPath:str, intSt:int) -> None:
#         self.intSt = intSt
#         self.lines = []
#         with open(strPlotPath, "r") as fp:
#             self.lines = fp.readlines()

#     def box(strMessage: str)->str:
#         return f"""
# <producer id="producer6" in="00:00:00.000" out="03:59:59.960">
#     <property name="length">04:00:00.000</property>
#     <property name="eof">pause</property>
#     <property name="resource">/Users/mattsunkun/Library/Application Support/Meltytech/Shotcut/autosave/#00000000</property>
#     <property name="aspect_ratio">1</property>
#     <property name="mlt_service">color</property>
#     <property name="mlt_image_format">rgba</property>
#     <property name="shotcut:caption">transparent</property>
#     <property name="shotcut:detail">transparent</property>
#     <property name="xml">was here</property>
#     <property name="seekable">1</property>
#     <property name="meta.shotcut.vui">1</property>
#     <filter id="filter4" out="00:00:06.640">
#       <property name="argument">まずは自己紹介軽く自己紹介．
# うp主は，「まっつんくん」という名前で活動しています．
# </property>
#       <property name="geometry">371 834 1505 211 1</property>
#       <property name="family">Hiragino Sans</property>
#       <property name="size">144</property>
#       <property name="weight">900</property>
#       <property name="style">normal</property>
#       <property name="fgcolour">#ffffffff</property>
#       <property name="bgcolour">#00000000</property>
#       <property name="olcolour">#aa000000</property>
#       <property name="pad">0</property>
#       <property name="halign">left</property>
#       <property name="valign">middle</property>
#       <property name="outline">3</property>
#       <property name="opacity">1</property>
#       <property name="mlt_service">dynamictext</property>
#       <property name="shotcut:filter">dynamicText</property>
#       <property name="shotcut:usePointSize">1</property>
#       <property name="shotcut:pointSize">144</property>
#     </filter>
#   </producer>
# """
#     def createBoxes(self)->None:
#         ans = []
#         boxMessage = []
#         for line in self.lines:
#             if(line == "<EOF>"):
#                 break
#             if(line == "<>"):
#                 ans.append(boxMessage)
#                 continue
#             boxMessage.append(line)
#         print(*ans, sep="\n")
#     def putOnLine():


def subtitle(strPlotPath:str, intSt:int)->None:
    cstrOUT = "00:00:17.560"
    with open(strPlotPath, "r") as fp:
        lsBox = []
        lsTimeline = []

        lsMessage = []
        for line in fp:
            
            line = line.rstrip()
            # print(line)
            # break
            if(line == "<EOF>"):
                break
            elif(line == "<>"):
                lsBox.append(f"""
<producer id="producer{intSt}" in="00:00:00.000" out="03:59:59.960">
    <property name="length">04:00:00.000</property>
    <property name="eof">pause</property>
    <property name="resource">/Users/mattsunkun/Library/Application Support/Meltytech/Shotcut/autosave/#00000000</property>
    <property name="aspect_ratio">1</property>
    <property name="mlt_service">color</property>
    <property name="mlt_image_format">rgba</property>
    <property name="shotcut:caption">transparent</property>
    <property name="shotcut:detail">transparent</property>
    <property name="xml">was here</property>
    <property name="seekable">1</property>
    <property name="meta.shotcut.vui">1</property>
    <filter id="filter{intSt}" out="{cstrOUT}">
      <property name="argument">{"n".join(lsMessage)}</property>
      <property name="geometry">371 834 1505 211 1</property>
      <property name="family">Hiragino Sans</property>
      <property name="size">144</property>
      <property name="weight">900</property>
      <property name="style">normal</property>
      <property name="fgcolour">#ffffffff</property>
      <property name="bgcolour">#00000000</property>
      <property name="olcolour">#aa000000</property>
      <property name="pad">0</property>
      <property name="halign">left</property>
      <property name="valign">middle</property>
      <property name="outline">3</property>
      <property name="opacity">1</property>
      <property name="mlt_service">dynamictext</property>
      <property name="shotcut:filter">dynamicText</property>
      <property name="shotcut:usePointSize">1</property>
      <property name="shotcut:pointSize">144</property>
    </filter>
  </producer>
""")
                
                lsTimeline.append(f"""
<entry producer="producer{intSt}" in="00:00:00.960" out="{cstrOUT}"/>
""")
                lsMessage = []
                intSt += 1
            else:
                lsMessage.append(line)
        print("<BOX>")
        print(*lsBox, sep="\n")
        print("<BOX>")
        print("<TIMELINE>")
        print(*lsTimeline, sep="\n")
        print("<TIMELINE>")
if __name__ == "__main__":
    subtitle("./plot.txt", 100)