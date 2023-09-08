import reflex as rx
import asyncio
from typing import List
import random


class State(rx.State):
    _blockHeight: int = 0
    msg_list: List[str] = [
        "Blockheight = ",
        "no errors found in ",
        "The weather is pretty nice today",
        "German is going to hate my code",
        "I don't know how people do this for a living",
        ]
    msgs: list[str]

    async def tick(self):
        """Update the blockheight every second."""
        self._blockHeight += 1
        if self.start:
            await asyncio.sleep(1)
            return self.tick

    def get_msg(self):
        blurb=random.choice(self.msg_list)
        if blurb == self.msg_list[0]:
            blurb = blurb + self.block_height
        return blurb

    def add_msg(self, msglist, msg):
        msglist.append(msg)
        if len(msglist) >20:
            del msglist[0]

    def updateConsoleText(self,msglist) -> rx.Component:
        self.add_msg(msglist, self.get_msg())
        return rx.List(msglist)

class baseChainState(State):
    msgs: list[str]

class sideChainState(State):
    msgs: list[str










